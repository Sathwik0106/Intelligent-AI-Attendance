import streamlit as st
from src.UI.base_layout import style_background_dashboard,base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

def teacher_screen():

    style_background_dashboard()
    base_layout()

    

    if 'teacher_login_type' not in st.session_state or st.session_state['teacher_login_type']=='login':
        teacher_screen_login()
    else:
        teacher_screen_register()
    
    


def teacher_screen_login():
    c1,c2=st.columns(2,vertical_alignment="center",gap='xxlarge')

    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back to home",key='loginbackbtn',shortcut="control+backspace"):
            st.session_state['login_type']='Home'
            st.rerun()
    
    st.header("Login using password",text_alignment='center')
    st.space()
    teacher_username=st.text_input("Enter username",placeholder="Enter your username")
    teacher_password=st.text_input("Enter password",placeholder="Enter your password",type='password')
    st.divider()

    btncol1,btncol2=st.columns(2)

    with btncol1:
        st.button('Login',icon=':material/passkey:',shortcut="control+enter",width='stretch')
            

    with btncol2:
        if st.button('Register Instead',type='primary',icon=':material/passkey:',shortcut="control+enter",width='stretch'):
            st.session_state['teacher_login_type']='register'
            st.rerun()
        
    
    footer_dashboard()


def teacher_screen_register():
    c1,c2=st.columns(2,vertical_alignment="center",gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back to home",key='loginbackbtn',shortcut="control+backspace",width='stretch'):
            st.session_state['login_type']='Home'
            st.rerun()
        
    
    
    st.header("Register your teacher profile",text_alignment='center')

    st.space()

    teacher_username=st.text_input("Enter username",placeholder="Enter your username")
    teacher_name=st.text_input("Enter your name",placeholder="Enter your name")
    teacher_password=st.text_input("Enter password",placeholder="Enter your password",type='password')
    teacher_password_confirm=st.text_input("Confirm your password",placeholder="Enter your password",type='password')
    
    if teacher_password!=teacher_password_confirm:
        st.error("Passwords do not match")
    st.divider()
    btnc1,btnc2=st.columns(2)

    with btnc1:
        st.button('Register Now',icon=':material/passkey:',shortcut="control+enter",width='stretch')
    
    with btnc2:
        if st.button("Login Instead",type='primary',icon=':material/passkey:',shortcut="control+enter",width='stretch'):
            st.session_state['teacher_login_type']='login'
            st.rerun()
    
    footer_dashboard()