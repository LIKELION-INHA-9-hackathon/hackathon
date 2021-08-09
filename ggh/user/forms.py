# from django import forms 
# from .models import *
# from django.contrib.auth.hashers import check_password
# from argon2 import PasswordHasher, exceptions


# # 회원가입 폼
# class CreateForm(forms.ModelForm):
#     user_email = forms.EmailField(
#         label = '이메일', 
#         required=True, 
#         widget =forms.TextInput(
#             attrs={
#                 'class' : 'user_email',
#                 'palceholder' : '이메일'
#             }
#         ), 
#         error_messages={'required' : '이메일 입력 해주세요'}
#     )
#     name = forms.CharField(
#         label = '이름', 
#         required=True, 
#         widget =forms.TextInput(
#             attrs={
#                 'class' : 'name',
#                 'palceholder' : '이름'
#             }
#         ), 
#         error_messages={'required' : '이름 입력 해주세요'}
#     )
#     nickname = forms.CharField(
#         label = '아이디 닉네임', 
#         required=True, 
#         widget =forms.TextInput(
#             attrs={
#                 'class' : 'nickname',
#                 'palceholder' : '아이디'
#             }
#         ), 
#         error_messages={'required' : '아이디 입력해주세요', 'unique' : '중복된 아이디입니다.'}
#     )
#     password = forms.CharField(
#         label = '비밀번호', 
#         required=True, 
#         widget =forms.PasswordInput(
#             attrs={
#                 'class' : 'password',
#                 'palceholder' : '비밀번호'
#             }
#         ), 
#         error_messages={'required' : '비밀번호 입력 해주세요'}
#     )
#     re_password = forms.CharField(
#         label = '비밀번호 다시', 
#         required=True, 
#         widget =forms.PasswordInput(
#             attrs={
#                 'class' : 're_password',
#                 'palceholder' : '비밀번호 다시'
#             }
#         ), 
#         error_messages={'required' : '비밀번호 다시 입력 해주세요'}
#     )

#     ph_no = forms.CharField(
#         label = '전화번호', 
#         required=True, 
#         widget =forms.TextInput(
#             attrs={
#                 'class' : 'ph_no',
#                 'palceholder' : '전화번호'
#             }
#         ), 
#         error_messages={'required' : '전화번호 입력 해주세요'}
#     )
#     birth = forms.CharField(
#         label = '생년월일', 
#         required=True, 
#         widget =forms.TextInput(
#             attrs={
#                 'class' : 'birth',
#                 'palceholder' : '생년월일'
#             }
#         ), 
#         error_messages={'required' : '생년월일 입력 해주세요'}
#     )
#     location = forms.CharField(
#         label = '주소', 
#         required=True, 
#         widget =forms.TextInput(
#             attrs={
#                 'class' : 'location',
#                 'palceholder' : '주소'
#             }
#         ), 
#         error_messages={'required' : '주소 입력 해주세요'}
#     )
#     # cabinet = forms.CharField(
#     #     label = '사물함', 
#     #     required=True, 
#     #     widget =forms.TextInput(
#     #         attrs={
#     #             'class' : 'cabinet',
#     #             'palceholder' : '사물함'
#     #         }
#     #     ), 
#     #     error_messages={'required' : '사물함 입력 해주세요'}
#     # )

#     class Meta : 
#         model = User
#         fields = [
#             'user_email', 
#             'name', 
#             'nickname', 
#             'password', 
#             'ph_no', 
#             'birth', 
#             'location',
#             'cabinet',
#             're_password',
#             'gender', 
#             'marketing',
#         ]
#     def clean(self):
#         cleaned_data =super().clean()

#         user_email=cleaned_data.get('user_email')
#         password=cleaned_data.get('password')
#         re_password=cleaned_data.get('re_password')
#         name=cleaned_data.get('name')
#         nickname=cleaned_data.get('nickname')
#         ph_no=cleaned_data.get('ph_no')
#         birth=cleaned_data.get('birth')
#         location=cleaned_data.get('location')
#         cabinet=cleaned_data.get('cabinet')
#         gender=cleaned_data.get('gender')
#         marketing=cleaned_data.get('marketing')

#         if password != re_password : 
#             return self.add_error('re_password', '비밀번호 다름')
#         elif not(4<=len(nickname)) :
#             return self.add_error('nickname', '아이디는 4~ 16자로 입력바람')
#         elif 8 >len(password):
#             return self.add_error('password', '비밀번호는 8자 이상으로 적어주세요. ')
#         else : 
#             self.nickname  = nickname
#             self.password = PasswordHasher().hash(password)
#             self.re_password = re_password
#             self.name = name 
#             self.user_email = user_email
#             self.ph_no = ph_no
#             self.birth = birth
#             self.location = location 
#             self.cabinet = cabinet
#             self.gender = gender
#             self.marketing = marketing

# ## 로그인 폼
# class LoginForm(forms.Form):
#     nickname = forms.CharField(
#         max_length=200, 
#         label='아이디', 
#         required=True, 
#         widget=forms.TextInput(
#             attrs ={
#                 'class' : 'nickname', 
#                 'placeholder' : '아이디'
#                 }
#         ),
#         error_messages={'required' : '아이디를 입력해주세요'}
#     )
#     password = forms.CharField(
#         max_length=200, 
#         label='비밀번호', 
#         required=True, 
#         widget=forms.PasswordInput(
#             attrs ={
#                 'class' : 'password', 
#                 'placeholder' : '비밀번호'
#                 }
#         ),
#         error_messages={'required' : '비밀번호를 입력해주세요'}
#     )

#     field_order=[
#         'nickname', 
#         'password',
#     ]
#     # # 유효성 검사 clean 메소드 오버라이드 
#     def clean(self): 
#         clean_data = super().clean()
#         nickname= clean_data.get('nickname','')
#         password = clean_data.get('password','')

#         if nickname =='' : 
#             return self.add_error('nickname', '아이디를 다시 입력해주세요')
#         elif password == '' : 
#             return self.add_error('password', '비밀번호를 다시 입력해주세요')

#         else : 
#             try : 
#                 user = User.objects.get(nickname = nickname)
#             except User.DoesNotExist:
#                 return self.add_error('nickname', '아이디가 존재하지 않습니다.')
            
#             try : 
#                 PasswordHasher().verify(user.password,password)
#             except exceptions.VerificationError:
#                 return self.add_error('password', '비밀번호가 다릅니다.')


# # class LoginForm(forms.Form):
# #     nickname = forms.CharField(max_length=200, label = "아이디", 
# #         error_messages={
# #             'required':"아이디를 입력하세요."
# #         })

# #     password = forms.CharField(label = "비밀번호", widget=forms.PasswordInput,
# #         error_messages ={
# #             'requied' : "비밀번호를 입력하세요"
# #     })
#         # # 회원 일치 조회 
#         # if nickname and password : # 둘다 None이 아니면
#         #     user = User.objects.get(nickname=nickname)

#         #     if not check_password(password, user.password):
#         #         self.add_error('password','비밀번호가 틀렸습니다.')
#         #     else :  
#         #         self.user_id = user.id

