import yt_dlp
import streamlit as st


def downloadvideo(url2):
        ydl_opts = {'format':'mp4[height<=800]', 'outtmpl': str('%(title)s - %(id)s.%(ext)s'), 'restrictfilenames':True, 'forcefilename':True,}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url2, download=True)
                main_title = info_dict['title']
                main_id = info_dict['id']
                video_name = ydl.prepare_filename(info_dict)
                return video_name
		

if __name__ == '__main__':
        st.subheader('Streamlit app')
        url = st.text_input('Enter the URL')
        url = url.replace(" ", "")
        if 'https' in url.lower() and (url[-13:-11] == 'v='):
                uid = url[-11:]
                st.text( 'format: HD' )
                vname = downloadvideo(uid)
                st.write(vname)
                st.video(f"./{vname}")

        else:
                st.text( r'please enter the url like this: https://www.youtube.com/v=...' )  
			
