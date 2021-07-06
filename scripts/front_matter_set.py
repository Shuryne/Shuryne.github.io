import shutil
import os
import re

import frontmatter
from tqdm import tqdm


# 原始文章地址
OriginDirPath = os.path.abspath('./scripts/posts_origin')

# 补全 Front Matter 之后的文章地址
DumpDirPath = os.path.abspath('./content/post')

# 文章 Front Matter 配置模版
PostMetadataTemplate = {
    'title': '',                # 文章标题 默认使用md文件名
    'date': None,               # 文章创建时间 创建新文章时的必填项
    'draft': False,             # 是否是草稿 默认是可发布文章
    'categories': [],           # 目录分类 默认使用文章一级目录
    'tags': [],                 # 标签分类 默认使用文章二级目录 可添加其他值
}

# md文件中必填的Key
RequiredKey = ['date']


def get_all_dir(path: str):
    """ 获取所有文件夹 """
    results = [t for t in os.listdir(path) if not os.path.isfile(os.path.join(path, t))]
    return results


def get_all_article(path: str):
    """ 获取所有md结尾的文章 """
    results = [t for t in os.listdir(path) if t.endswith('md')]
    return results


def complete_front_matter():
    """ 自动补全文章 Front Matter """ 
    return


def front_matter_set(blog_dir: str):
    """ 
    自动化脚本: 给每篇文章自动补充 Front Matter 节省时间
    """
    print('Begin Auto Complete Front Matter...')
    print('Origin blog dir path: ', OriginDirPath)
    print('Dump blog dir path: ', DumpDirPath)

    blog_num = 0

    # 一级目录
    first_category_names = get_all_dir(blog_dir)
    # print('first_category_names', first_category_names)

    for first_category_name in tqdm(first_category_names[:]):
        first_category_path = os.path.join(blog_dir, first_category_name)
        
        # 二级目录
        second_category_names = get_all_dir(first_category_path)
        # print('second_category_names', second_category_names)
        
        for second_category_name in second_category_names[:]:
            second_category_path = os.path.join(first_category_path, second_category_name)
            dump_dir = os.path.join(DumpDirPath, first_category_name, second_category_name)
            for file in os.listdir(dump_dir):
                os.remove(os.path.join(dump_dir, file))

            # 文章
            article_names = get_all_article(second_category_path)
            # print('article_names', article_names)

            for article_name in article_names:
                blog_num += 1
                article_path = os.path.join(second_category_path, article_name)
                post = frontmatter.load(article_path)
                
                # step 0: valid check                
                for key in RequiredKey:
                    assert key in post.metadata

                # print('article_name', article_name)
                # step 1: generate and override front matter
                metadata = PostMetadataTemplate.copy()
                # metadata = post.metadata
                metadata.update({
                    'title': re.sub(r'\.md$', '', article_name),
                    'categories': [first_category_name],
                    'tags': [second_category_name],
                })
                for k, v in post.metadata.items():
                    metadata[k] = v
                    # if k in ['categories', 'tags']:
                    #     metadata[k] += v
                    # else:
                    #     metadata[k] = v
                post.metadata = metadata
                # print(post.metadata)

                # step 3: remove dir and dump to new file
                dump_file = open(os.path.join(dump_dir, article_name), 'wb+')
                # dump阶段 front matter包会按key进行sort输出
                # 此处为了保证格式正确 修改了包的底层代码 按照template的顺序输出结果
                frontmatter.dump(post, dump_file)
                dump_file.close()

    print(f'{blog_num} Blog Article Generated...')
    print('End Auto Complete Front Matter...')


def main():
    # print(os.path.abspath('./content/posts_origin'))
    # print(os.path.abspath('./scripts/posts_origin'))
    front_matter_set(OriginDirPath)
    # data_path = '/Users/gungnir/Google/hugo-blog/scripts/posts_origin/无聊的幻想家/杂的文/随想——一二九.md'
    # post = frontmatter.load(data_path)
    # print(post.content)


if __name__ == '__main__':
    main()
