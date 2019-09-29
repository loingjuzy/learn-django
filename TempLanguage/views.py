from django.shortcuts import render
from django.utils.safestring import mark_safe

LIST = []
for i in range(199):
    LIST.append(i)


def user_list(request):
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)

    start = (current_page - 1) * 10
    end = current_page * 10
    data = LIST[start:end]

    all_count = len(LIST)
    total_count, y = divmod(all_count, 10)
    if y:
        total_count += 1
    pager_num = 11  # 页码数

    page_list = []
    if total_count < pager_num:  # 总页面小于页码数
        start_index = 1
        end_index = total_count + 1
    else:
        if current_page <= pager_num / 2:  # 开头
            start_index = 1
            end_index = pager_num + 1
        elif current_page + (pager_num - 1) / 2 >= total_count:  # 中间
            start_index = total_count - (pager_num - 1)
            end_index = total_count + 1
        else:  # 结尾
            start_index = current_page - (pager_num - 1) / 2
            end_index = current_page + (pager_num - 1) / 2 + 1

    # 上下页码
    if current_page == 1:
        prev = '<a class="page" href="javascript:void(0)">上一页</a>'  # 什么都不干
    else:
        prev = '<a class="page" href="/user_list/?p=%s">上一页</a>' % (current_page - 1)
    page_list.append(prev)
    for i in range(int(start_index), int(end_index)):
        if i == current_page:
            temp = '<a class="page active" href="/user_list/?p=%s">%s</a>' % (i, i)
        else:
            temp = '<a class="page" href="/user_list/?p=%s">%s</a>' % (i, i)

        page_list.append(temp)
    if current_page == total_count:
        nex = '<a class="page" href="javascript:void(0)">下一页</a>'  # 什么都不干
    else:
        nex = '<a class="page" href="/user_list/?p=%s">下一页</a>' % (current_page + 1)
    page_list.append(nex)

    # 跳转 可以写到前端
    jump = '''
    <input type="text" /><a onclick="jumpTo(this,'/user_list/?p=');">GO</a>
    <script>
        function jumpTo(ths,base) {
            var val = ths.previousSibling.value;
            location.href = base + val;
        }
    </script>
    '''
    page_list.append(jump)

    page_str = mark_safe(''.join(page_list))

    return render(request, 'user_list.html', {'li': data, 'page_str': page_str})
