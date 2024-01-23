"""
Time    : 2024/1/23 11:06 
file    : allkindscode.py
Author  : qychui
"""
from django.shortcuts import render, redirect
from app01.utils.page_nav import PageNav
from app01.srcs.forms.form import NumModelForm, NumModelFormEdit, UserModelForm, CodeModelForm


def test_add(request):
    search_data_dict = { }
    search_data = request.GET.get("q", "")
    page = int(request.GET.get("page", "1"))  # 第二个参数表示默认数值
    start_page = page - 5
    end_page = page + 5

    if search_data:
        search_data_dict["mobile__contains"] = search_data
    content = {
        # "queryset": page_queryset,
        "search_data": search_data,
        # "page_nav_string": page_nav_string,
    }
    return render(request, "allkindscode/code_management.html", content)


def add_product_code(request):
    if request.method == "GET":
        form = CodeModelForm()
        content = {
            "form": form
        }
        return render(request, "allkindscode/code_add.html", content)
    form = CodeModelForm(data=request.POST)
    if form.is_valid():
        # form.instance.字段名 = 手动赋值
        form.save()
        return redirect("/allkindscode/management")
    return render(request, "allkindscode/code_add.html", {"form": form})
