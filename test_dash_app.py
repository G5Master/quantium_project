import app

#Test 1: Check the presents of the header element
def test_is_header_present(dash_duo):
     #Run the app locally in a thread
     dash_duo.start_server(app.app)
     
     #Find the header element 
     dash_duo.wait_for_element("h1",timeout=4)
     header=dash_duo.find_element("h1")
     
     #Check if the header element is present
     assert header.text=="Pink Morsel Price Versus Sales"

#Test 2: Check the presents of the visualisation(line-chart)
def test_is_visualisation_present(dash_duo):
     #Run the app in a thread 
     dash_duo.start_server(app.app)
     
     #Find the line chart element
     dash_duo.wait_for_element("#line-chart",timeout=4)
     line=dash_duo.find_element("#line-chart")
     
     #Check if the line chart found exists
     assert line is not None
     
#Test 3: Check the presence of the region picker(radio items)
def test_is_region_picker_present(dash_duo):
     #Run the app in a thread
     dash_duo.start_server(app.app)

     #find the radio items
     dash_duo.wait_for_element("#region-items",timeout=4)
     radio_items=dash_duo.find_element("#region-items") 

     #Check if the radio_items exist     
     assert radio_items is not None   
     
     