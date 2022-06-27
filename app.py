import yt_dlp
import streamlit as st


if __name__ == '__main__':
        st.subheader('Streamlit app')
        url = st.text_input('Enter the URL')
        url = url.replace(" ", "")
        if 'https' in url.lower() and (url[-13:-11] == 'v='):
                ydl_opts = {'format':'mp4[height<=800]', 'outtmpl': str('%(title)s - %(id)s.%(ext)s'), 'restrictfilenames':True, 'forcefilename':True,}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info_dict = ydl.extract_info(url, download=True)
                        video_name = ydl.prepare_filename(info_dict)
                st.write(video_name)
                st.video(f"./{video_name}")

        else:
                st.text( r'please enter the url like this: https://www.youtube.com/v=...' )  
			
