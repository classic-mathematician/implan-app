from typing import Container
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd 
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import folium
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

denue2018 = pd.read_csv('https://raw.githubusercontent.com/classic-mathematician/avocado/main/DENUE_2018.csv')
denue2019 = pd.read_csv('https://raw.githubusercontent.com/classic-mathematician/avocado/main/DENUE_2019.csv')
denue2020 = pd.read_csv('https://raw.githubusercontent.com/jgibranv/implang/main/DENUE/DENUE_2020.csv')
inegi2010 = pd.read_csv('https://raw.githubusercontent.com/jgibranv/implang/main/INEGI/INEGI_2010.csv')
inegi2020 = pd.read_csv('https://raw.githubusercontent.com/jgibranv/implang/main/INEGI/INEGI_2020.csv')

#Analisis del 2018
df18 = denue2018[['ageb', 'nom_estab']]
df18g = df18.groupby(['ageb'], as_index=False).count()
asent18 = denue2018[['nomb_asent', 'nom_estab']]
asent18 = asent18.groupby(['nomb_asent'], as_index=False).count().sort_values(by=['nom_estab'], ascending=False)
asent18 = asent18[1:10]

#Analisis del 2019
df19 = denue2019[['ageb', 'nom_estab']]
df19g = df19.groupby(['ageb'], as_index=False).count()
asent19 = denue2019[['nomb_asent', 'nom_estab']]
asent19 = asent19.groupby(['nomb_asent'], as_index=False).count().sort_values(by=['nom_estab'], ascending=False)
asent19 = asent19[1:10]

#Analisis del 2020
df20 = denue2020[['ageb', 'nom_estab']]
df20g = df20.groupby(['ageb'], as_index=False).count()
asent20 = denue2020[['nomb_asent', 'nom_estab']]
asent20 = asent20.groupby(['nomb_asent'], as_index=False).count().sort_values(by=['nom_estab'], ascending=False)
asent20 = asent20[1:10]

#Mapas
#Concatenacion de los 3 archivos en uno solo
denue2018['year'] = 2018
denue2019['year'] = 2019
denue2020['year'] = 2020
DENUEgj = pd.concat([denue2018,denue2019,denue2020])

#Se corrigen los typos con regex
DENUEgj["per_ocu"] = DENUEgj["per_ocu"].replace("251 y m.s personas|251 y m..s personas", "251 y mas personas", regex=True)




#Funciones
def ageb2018():
    fig = px.bar(df18g, x='ageb', y='nom_estab')

    fig = px.bar(df18g,
                     x='ageb',
                     y='nom_estab',
                     template='plotly_dark').update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                         'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    fig.update_xaxes(type='category')
    return dcc.Graph(id="graph-ageb2018", figure=fig)

def nombreAsentamiento2018():
    fig = px.pie(asent18,
                 values='nom_estab',
                 names='nomb_asent',
                 template='plotly_dark').update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                         'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return dcc.Graph(id="graph-nombreAsentamiento2018", figure=fig)

def ageb2019():
    fig = px.bar(df19g,
                     x='ageb',
                     y='nom_estab',
                     template='plotly_dark').update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                         'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_xaxes(type='category')
    return dcc.Graph(id="graph-ageb2019", figure=fig)

def nombreAsentamiento2019():
    fig = px.pie(asent19,
                 values='nom_estab',
                 names='nomb_asent',
                 template='plotly_dark').update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                         'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return dcc.Graph(id="graph-nombreAsentamiento2019", figure=fig)   

def ageb2020():
    fig = px.bar(df20g,
                     x='ageb',
                     y='nom_estab',
                     template='plotly_dark').update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                         'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_xaxes(type='category')
    return dcc.Graph(id="graph-ageb2020", figure=fig)

def nombreAsentamiento2020():
    fig = px.pie(asent20,
                    values='nom_estab',
                    names='nomb_asent',
                    template='plotly_dark').update_layout(
                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                        'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return dcc.Graph(id="graph-nombreAsentamiento2020", figure=fig)

def unidadesXageb():
    mapa =  px.scatter_mapbox(DENUEgj, lat="latitud", lon= "longitud", color='ageb',
                         animation_frame="year",
                         color_discrete_sequence=px.colors.qualitative.Safe,
                         size_max=10,
                         mapbox_style='carto-positron',
                         zoom=11,
                         template='plotly_dark').update_layout(
                            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                            'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return dcc.Graph(id="map-unidadesXageb", figure=mapa)

def unidadesxFijos():
    mapa =  px.scatter_mapbox(DENUEgj, lat="latitud", lon= "longitud", color='tipoUniEco',
                         animation_frame="year",
                         color_discrete_sequence=px.colors.qualitative.Safe,
                         size_max=10,
                         mapbox_style='carto-positron',
                         zoom=11,
                         template='plotly_dark').update_layout(
                            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                            'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return dcc.Graph(id="map-unidadesXfijos", figure=mapa)

def ocupacion():
    mapa =  px.scatter_mapbox(DENUEgj, lat="latitud", lon= "longitud", color='per_ocu',
                         animation_frame="year",
                         color_discrete_sequence=px.colors.qualitative.Safe,
                         size_max=10,
                         mapbox_style='carto-positron',
                         zoom=11,
                         template='plotly_dark').update_layout(
                            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                            'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return dcc.Graph(id="map-ocupacion", figure=mapa)

def densidad():
    fig = px.density_mapbox(DENUEgj, lat='latitud', lon='longitud', 
                        radius=5,
                        animation_frame="year",
                        zoom=12,
                        mapbox_style="carto-positron",
                        color_continuous_scale = px.colors.sequential.PuBu,
                        width = 1000,
                        height = 900,
                        template='plotly_dark').update_layout(
                            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                            'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return dcc.Graph(id="map-densidad", figure=fig)

def negocios():
    #2018
    df18 = denue2018[['ageb', 'nom_estab', 'latitud', 'longitud']]
    df18_count = df18.groupby(['ageb'], as_index=False).count()
    df18_sum = df18.groupby(['ageb'], as_index=False).sum()
    df18_count['latitud'] = df18_sum['latitud'] / df18_count['latitud']
    df18_count['longitud'] = df18_sum['longitud'] / df18_count['longitud']
    df18_count['Cantidad de Negocios'] = df18_count['nom_estab']
    df18_dif = (df18_count["Cantidad de Negocios"].max() - df18_count["Cantidad de Negocios"].min()) / 16
    df18_count["scale"] = (df18_count["Cantidad de Negocios"] - df18_count["Cantidad de Negocios"].min()) / df18_dif 

    #2019
    df19 = denue2019[['ageb', 'nom_estab', 'latitud', 'longitud']]
    df19_count = df19.groupby(['ageb'], as_index=False).count()
    df19_sum = df19.groupby(['ageb'], as_index=False).sum()
    df19_count['latitud'] = df19_sum['latitud'] / df19_count['latitud']
    df19_count['longitud'] = df19_sum['longitud'] / df19_count['longitud']
    df19_count['Cantidad de Negocios'] = df19_count['nom_estab']
    df19_dif = (df19_count["Cantidad de Negocios"].max() - df19_count["Cantidad de Negocios"].min()) / 16
    df19_count["scale"] = (df19_count["Cantidad de Negocios"] - df19_count["Cantidad de Negocios"].min()) / df19_dif 

    #2020
    df20 = denue2020[['ageb', 'nom_estab', 'latitud', 'longitud']]
    df20_count = df20.groupby(['ageb'], as_index=False).count()
    df20_sum = df20.groupby(['ageb'], as_index=False).sum()
    df20_count['latitud'] = df20_sum['latitud'] / df20_count['latitud']
    df20_count['longitud'] = df20_sum['longitud'] / df20_count['longitud']
    df20_count['Cantidad de Negocios'] = df20_count['nom_estab']
    df20_dif = (df20_count["Cantidad de Negocios"].max() - df20_count["Cantidad de Negocios"].min()) / 16
    df20_count["scale"] = (df20_count["Cantidad de Negocios"] - df20_count["Cantidad de Negocios"].min()) / df20_dif 

    df18_count['year'] = 2018
    df19_count['year'] = 2019
    df20_count['year'] = 2020
    df_count = pd.concat([df18_count,df19_count,df20_count])

    mapa =  px.scatter_mapbox(df_count, lat="latitud", lon= "longitud",
                         animation_frame="year",
                         color='Cantidad de Negocios',
                         hover_name="ageb", 
                         hover_data=["ageb", "Cantidad de Negocios"], 
                         color_continuous_scale=px.colors.sequential.Purples,
                         size_max=50,
                         size=df_count["scale"],
                         mapbox_style='carto-positron', title='Cantidad de Negocios por AGEB',
                         zoom=12,
                         range_color = [-200,300],
                         width = 1000,
                         height = 900,
                         template='plotly_dark').update_layout(
                            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                            'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    return dcc.Graph(id="map-negocios", figure=mapa)


app = dash.Dash(__name__)



app.layout = html.Div([

    ####################################### COMIENZA ESPACIO DE EDICIÓN #######################################

    ## BANNER PRINCIPAL
    dbc.Container([

        dbc.Row(


            dbc.Col([

                html.Center(html.H1("Visualización Implan", style={'display': 'inline-block'})),

                html.A(
                    html.Center(html.Img(src='../assets/sanpedro.jpg', style={'display': 'inline-block'})),
                href='https://www.instagram.com/implang_spgg/', target='blank'
                ),

            ]), className='px-1 py-4'



        ),


        dbc.Row(
            dbc.Col(

                html.Center(html.H2("Análisis de DENUE 2018"))
            ),
        ),
        dbc.Row(
            dbc.Col(
                ageb2018(),
            ),

        ),
        dbc.Row(
            dbc.Col(
                html.H5("")
            )
        ),
        dbc.Row(
            dbc.Col(
                nombreAsentamiento2018()
            )
        ),

    ]),

    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.Center(html.H2("Análisis de DENUE 2019"))
            )
        ),
        dbc.Row(
            dbc.Col(
                ageb2019()
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.H5("")
            )
        ),
        dbc.Row(
            dbc.Col(
                nombreAsentamiento2019()
            )
        ),

    ]),

    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.Center(html.H2("Análisis de DENUE 2020"))
            )
        ),
        dbc.Row(
            dbc.Col(
                ageb2020()
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.H5("")
            )
        ),
        dbc.Row(
            dbc.Col(
                nombreAsentamiento2020()
            )
        ),

    ]),

    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.H2("Unideades Economicas por Fecha de Alta")
            )
        ),
        dbc.Row(
            dbc.Col(
                unidadesXageb()
            ),
        ),

    ]),

    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.H2("Unidades Económicas entre Fijos y Semifijos")
            )
        ),
        dbc.Row(
            dbc.Col(
                unidadesxFijos()
            ),
        ),

    ]),

    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.H2("Unidades Económicas por Ocupación")
            )
        ),
        dbc.Row(
            dbc.Col(
                ocupacion()
            ),
        ),

    ]),

    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.H2("Densidad de Negocios")
            )
        ),
        dbc.Row(
            dbc.Col(
                densidad()
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.H5("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent in iaculis justo, vitae rutrum urna. Maecenas egestas fermentum augue id mollis.")
            )
        ),
    ]),

    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.H2("Negocios por AGEB")
            )
        ),
        dbc.Row(
            dbc.Col(
                negocios()
            ),
        ),

    ]),




##################################### TERMINA ESPACIO DE EDICIÓN ########################################

    # Footer
    dbc.Container([
    
        dbc.Row(
            dbc.Col(
              html.H6('Envíanos un correo a implang@sanpedro.gob.mx')  
            ), className='px-1 pt-4'
        ),

        dbc.Row(
            dbc.Col([
                html.A(
                    html.Img(src='../assets/instagram.png', style={'max-width':'85px', 'height':'34px'}),
                    href='https://www.instagram.com/implang_spgg/', target='blank'
                ),

                html.A(
                    html.Img(src='../assets/facebook.png', style={'max-width':'85px', 'height':'34px'}),
                    href='https://www.facebook.com/implangspgg', target='blank', className='pl-3'
                ),

                html.A(
                    html.Img(src='../assets/twitter.png', style={'max-width':'85px', 'height':'34px'}),
                    href='https://twitter.com/implang_spgg', target='blank', className='pl-3'
                ),

                html.A(
                    html.Img(src='../assets/youtube.png',style={'max-width':'85px', 'height':'34px'}),
                    href='https://www.youtube.com/channel/UCZwYFPh0dHnKhXqzaxlaqNg', target='blank',
                    className='pl-3'
                )
            ]), className='px-1 py-4'
        )
        
    ]),

    dbc.Container([

       dbc.Row(
            dbc.Col(
                html.H6('Instituto Municipal de Planeación y Gestión Urbana')
            ), className='px-1 pt-3'
        ),

        dbc.Row(
            dbc.Col(
                html.H6('San Pedro Garza García, Nuevo León, México')
            ), className='px-1 py-3'
        )
        
    ], style={'background-color': 'black','color': 'white'}
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)