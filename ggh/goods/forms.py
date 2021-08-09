from django import forms
from .models import Goods


class CreateForm(forms.ModelForm):
    title = forms.CharField(
        label ='글 제목', 
        widget = forms.TextInput(
            attrs={
                'placeholder' : '게시글 제목'
            }),
        required=True,
        )
    
    class Meta : 
        model = Goods
        fields = [
            'name', 
            'sale_price', 
            'norm_price', 
            'type', 
            'category', 
            'tags', 
            'title',
            'content', 
            'recruitment_no', 
            'deadline', 
            'image', 
            'url'
        ]

    def clean(self) : 
        cleaned_data = super().clean() # super() :  부모 클래스의 생성자를 호출하는 메서드

        name = cleaned_data.get('name')
        sale_price = cleaned_data.get('sale_price')
        norm_price = cleaned_data.get('norm_price')
        type = cleaned_data.get('type')
        category = cleaned_data.get('category')
        tags=cleaned_data.get('tags')
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        recruitment_no = cleaned_data.get('recruitment_no')
        deadline = cleaned_data.get('deadline')
        image=cleaned_data.get('image')
        url=cleaned_data.get('url')


        if title =='' : 
            return self.add_error('title,' '글 제목을 입력하세요')
        elif content == '' : 
            return self.add_error('content', '글 내용을 입력하세요.')
        elif sale_price == '' : 
            return self.add_error('sale_price', '공구 가격을 입력하세요.')
        elif recruitment_no == '' : 
            return self.add_error('recruitment_no', '모집인원을 입력하세요.')
        elif deadline =='' : 
            return self.add_error('deadline' ,'마감 기간을 입력하세요')

        else :
            self.name = name
            self.sale_price = sale_price
            self.norm_price = norm_price
            self.type = type
            self.category = category
            self.tags= tags
            self.title = title
            self.content = content
            self.recruitment_no = recruitment_no
            self.deadline =  deadline
            self.image= image
            self.url= url