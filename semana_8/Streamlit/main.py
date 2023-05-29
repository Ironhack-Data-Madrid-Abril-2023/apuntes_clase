import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io


st.title('Clase Streamlit')


st.header('Metodos para introducir texto')


st.subheader('Existen varios metodos para el texto')


st.write('introducir texto')

st.write('# Si ponemos "#" es como un h1')
st.write('## Si ponemos "##" es como un h2')
st.write('### Si ponemos "###" es como un h3')


st.info('Esto ya casi esta')
st.error('Esta clase ya casi esta.')
st.success('Esta clase ya casi esta.')
st.warning('Esta clase ya casi esta.')


df=pd.read_csv('src/data/comunio_J6.csv')
st.caption('# Podemos cargar un dataframe y mostrarlo')


filtros, equipos, pos, goles = st.columns(4)


with filtros:
    columnas = df.columns
    selection = st.multiselect('Filtrar Columnas', columnas, default=['Team',
                                                                      'Player', 
                                                                      'Position', 
                                                                      'Matchs', 
                                                                      'Goals',
                                                                      'Total_Points'])


with equipos:
    equipo = st.selectbox('Filtrar Equipos', df.Team.unique())

with pos:
    player_pos = st.selectbox('Filtrar Posicion', df.Position.unique())



with goles:
    gol_min, gol_max = st.select_slider('Filtrar por Goles', 
                                        options=[i for i in range(0,df.Goals.max()+1)],
                                        value=[0, df.Goals.max()])



st.sidebar.header('Menu Lateral')
st.sidebar.subheader('Streamlit Workshop for IH')
st.sidebar.image(Image.open('src/images/ih.png'))
st.sidebar.info('Aquí puedes poner una barra de navegación o zonas para cargar archivos')



uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
upload_image = st.sidebar.file_uploader('Upload an Image', type=['png', 'jpeg', 'jpg'])



if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)

else:
    df1 = df[selection]

    var = df1[(df1.Team == equipo) &
              (df1.Goals >= gol_min) &
              (df1.Goals <= gol_max) &
              (df1.Position == player_pos)]

    st.dataframe(var)

    df_plot = df1[(df1.Team == equipo) &
        (df1.Goals >= gol_min) &
        (df1.Goals <= gol_max) &
        (df1.Position == player_pos)]
    
    fig, ax = plt.subplots()
    plt.title(f'Puntos Totales del {equipo} por Jugador - Posición {player_pos}')
    ax.barh(y=df_plot.Player, width=df_plot.Total_Points)

    st.caption('## También podemos mostrar gráficos')
    st.pyplot(fig)


    
st.caption('## Imágenes')
if upload_image is not None:
    st.image(upload_image)
else:
    st.image(Image.open('src/images/ih.png'))



url = 'https://www.ironhack.com'
st.caption('## Podemos incluir un boton de redireccion')

if st.button('WEB IRON'):
    webbrowser.open_new_tab(url)

df_plot = df1[(df1.Team == equipo) &
        (df1.Goals >= gol_min) &
        (df1.Goals <= gol_max) &
        (df1.Position == player_pos)]
    
fig, ax = plt.subplots()
plt.title(f'Puntos Totales del {equipo} por Jugador - Posición {player_pos}')
ax.barh(y=df_plot.Player, width=df_plot.Total_Points)

img=io.BytesIO()
plt.savefig(img, format='png')
img.seek(0)
plot_url=base64.b64encode(img.getvalue()).decode()

html = f"<a href='{url}'><img src='data:image/png;base64,{plot_url}'></a>"
st.markdown(html, unsafe_allow_html=True)


st.video('https://www.youtube.com/watch?v=zS5pjxseTQM&list=RDzS5pjxseTQM&start_radio=1&ab_channel=JoanAsPoliceWoman')





