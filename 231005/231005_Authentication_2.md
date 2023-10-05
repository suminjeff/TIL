## 회원가입
- UserCreationForm() -> CustomUserCreationForm(UserCreationForm())
- Meta -> Meta(UserCreationForm.Meta)
- built-in ModelForm이기 때문에 model이 내장 auth.User 임 (커스텀 모델을 등록해줘야함)
- model = get_user_model()    # User라고 작성하는 것은 권장하지 않음

## 회원탈퇴
- User 객체를 delete
- request.user.delete()
- logout(request, )

## 회원정보수정
- UserChangeForm() -> CustomUserChangeForm(UserChangeForm())
- Meta -> Meta(UserChangeForm.Meta)
- instance = request.user

## 비밀번호 변경
- PasswordChangeForm(request.user)  <- 첫번째 인자 항상 User
- update_session_auth_hash(request, user) <- 암호 변경 시 세션 무효화를 막아줌