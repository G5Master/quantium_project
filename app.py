from dash import Dash,html,dcc
import pandas as pd
import plotly.express as px

#Initialize the dash app
app=Dash()

#Set up sample data
data_frame=pd.read_csv("./data/output_file.csv")

#Set up the layout of the application
app.layout=html.Div(

                     children=[
                               html.H1(  
                                        children="Pink Morsel Price Versus Sales"
                                      ),
                                #Use dcc.Graph to display the line chart 
                                dcc.Graph(
                                           id="line-chart",
                                           figure=px.line(data_frame,x="date",y="sales")  
                                            ) 

                              ]


                    )


#Run the web application
if __name__=="__main__":
   app.run(debug=True)