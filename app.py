from dash import Dash,html,dcc,Output,Input
import pandas as pd
import plotly.express as px

#Initialize the dash app
app=Dash()

#Set up sample data
data_frame=pd.read_csv("./data/output_file.csv")

#Sort out the data frame
data_frame=data_frame.sort_values(by="date")

#define color_discrete_map variable to distinguish the different line chart based on the region they are representing
color_discrete_map1={
                    "north":"blue",  
                     "south": "red",
                     "east ": "purple",
                     "west": "green"
                     }

#Set up the layout of the application
app.layout=html.Div(

                     children=[
                               html.H1(  
                                        children="Pink Morsel Price Versus Sales"
                               
                                      ),
                                #Use dcc.Graph to display the line chart 
                                dcc.Graph(
                                           id="line-chart",
                                           figure=px.line(data_frame,x="date",y="sales",color="region")
                                                                 
                                            ),
                                            
                                 html.Label(children=" Which region's sales do you want yo analyze ?")          
                                            
                                            
                                            ,

                                dcc.RadioItems( id="region-items", 
                                               options=[ "north","east",
                                                         "south","west",
                                                          "all"
                                                        ]  
                                               )                                            

                              ],
                              
                        style={ "backgroundColor": "grey"}      


                    )
#Handle the reatibility of the web page
@app.callback(
              Output("line-chart","figure"),
              Input("region-items","value")
          )

#Define method to update the line chart based on the selected radio item
def update_line_chart(selected_radio_item):
    if selected_radio_item=="all":
       #keep the updated data frame df the same the old data frame
       df=data_frame

    else:
        #update the data frame based on the selected radio item 
        df=data_frame[data_frame["region"]==selected_radio_item]        
    
    #Now sketch the updated line chart
    figure=px.line(df,x="date",y="sales",color="region",color_discrete_map=color_discrete_map1)
    return figure 
     
#Run the web application
if __name__=="__main__":
   app.run(debug=True)