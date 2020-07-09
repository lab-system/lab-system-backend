# author: gongjichao
# createTime: 2020/7/1 9:16

import os
import pathlib
import random
import sys
from datetime import timedelta, date

import django
import faker
from django.utils import timezone

# 将项目的根目录添加到Python的模块搜索路径中
back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__))) # 当前目录的上上级目录就是根目录
sys.path.append(BASE_DIR)

if __name__ == '__main__': # 可运行脚本文件
    # 设置环境变量，并启动django，否则无法使用ORM系统
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab_system_backend.settings")
    django.setup()

    def calculate_age(born):
        today = date.today()
        try:
            birthday = born.replace(year=today.year)
        except ValueError:
            # raised when birth date is February 29
            # and the current year is not a leap year
            birthday = born.replace(year=today.year, day=born.day - 1)
        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year

    from article.models import Category, Article, Tag
    from members.models import Classification, Member
    from users.models import UserProfile

    # 每次运行脚本时，清空原有数据
    print('clean database')
    Article.objects.all().delete()
    Category.objects.all().delete()
    Tag.objects.all().delete()

    Member.objects.all().delete()
    Classification.objects.all().delete()
    # UserProfile.objects.all().delete()

    # 创建超级用户
    # print('create a blog user')
    # user = UserProfile.objects.create_superuser('admin', 'admin@admin.admin', '123456')

    # 初始化分类和标签列表
    category_list = ['最新消息', '毕业咨询', '实验室简介', '研究方向', '开设课程', '硕士研究生培养', '博士研究生培养', '重大课题',
                     '国家级课题', '省部级课题', '横向课题', '科研掠影', '研究趣闻', '文艺作品', '文体活动', '设施设备', '开放共享',
                     '科普教育']
    tag_list = ['公告栏', '实验室概况', '科研队伍', '人才培养', '科研项目', '实验室文化', '资源共享']

    class_list = ['学术骨干', '固定流研究人员', '流动研究人员', '现任领导', '历任领导', '学术委员会']

    a_year_ago = timezone.now() - timedelta(days=365)

    # 创建分类和标签
    print('create categories and tags')
    for cate in category_list:
        Category.objects.create(name=cate)

    for tag in tag_list:
        Tag.objects.create(name=tag)

    for classify in class_list:
        Classification.objects.create(name=classify)

    # 创建一篇markdown的样例文章
    print('create a markdown sample post')
    article = Article.objects.create(
        title='数据导入测试',
        content=pathlib.Path(BASE_DIR).joinpath('scripts', 'md.sample').read_text(encoding='utf-8'), # 文章的正文从md.sample文件中获取
        category=Category.objects.create(name='最新消息'),
        author=UserProfile.objects.first(),
    )

    # 使用fake自动创建100篇文章
    print('create some faked posts published within the past year')
    fake = faker.Faker('zh_CN') # 默认是英文，现在是汉语
    article_id = 0
    for _ in range(100):
        tag = Tag.objects.order_by('?').first() # 随机排序标签
        cate = Category.objects.order_by('?').first() # 分配随机分类
        create_time = fake.date_time_between(start_date='-1y', end_date="now",
                                             tzinfo=timezone.get_current_timezone()) # 时间范围1年前， 现在， 时区
        article_id += 1
        post = Article.objects.create(
            title=fake.sentence().rstrip('.'),   # 每段结尾用.分割
            # content='\n\n'.join(fake.paragraphs(10)), # markdown的分段是两个回车符
            article_id=article_id,
            content=fake.text(max_nb_chars=600),
            create_time=create_time,
            category=cate,
            tags=tag,
            author=UserProfile.objects.first(),
        )
        post.save()

    # 创建成员
    print('create some members')
    member_id = 0
    for _ in range(20):
        classify = Classification.objects.order_by('?').first()
        create_time = fake.date_time_between(start_date='-1y', end_date="now",
                                             tzinfo=timezone.get_current_timezone())  # 时间范围1年前， 现在， 时区
        member_id += 1
        member = Member.objects.create(
            name=fake.name(),
            birthday=fake.date_object(),
            gender='male',
            phone=fake.phone_number(),
            member_type='student',
            category=classify,
            introduction=fake.paragraphs(10),
            create_time=create_time,
            member_id=member_id
        )
        member.save()

    # # 创建评论
    # print('create some comments')
    # for post in Post.objects.all()[:20]: # 给前20篇文章创建评论
    #     post_created_time = post.create_time
    #     delta_in_days = '-' + str((timezone.now() - post_created_time).days) + 'd' # 文章创建的时间到现在的差
    #     for _ in range(random.randrange(3, 15)): # 随机创建3-15条评论
    #         Comment.objects.create(
    #             name=fake.name(),
    #             email=fake.email(),
    #             url=fake.uri(),
    #             text=fake.paragraph(),
    #             create_time=fake.date_time_between(
    #                 start_date=delta_in_days, # 评论的时间在文章发布之后到现在之前
    #                 end_date="now",
    #                 tzinfo=timezone.get_current_timezone(),
    #             ),
    #             post=post,
    #         )

    print('done!')

