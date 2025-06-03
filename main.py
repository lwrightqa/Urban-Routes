# ---------- Task 3 ----------/
import data
import helpers

# ---------- Task 4 ---------- /
class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        print("function created for set route")
        pass # Add in Sprint 8
    def test_select_plan(self):
        print("function created for select plan")
        pass # Add in Sprint 8
    def test_fill_phone_number(self):
        print("function created for fill phone number")
        pass # Add in Sprint 8
    def test_fill_card(self):
        print("function created for fill card")
        pass # Add in Sprint 8
    def test_comment_for_driver(self):
        print("function created for comment for driver")
        pass # Add in Sprint 8
    def test_order_blanket_and_handkerchiefs(self):
        print("function created for order blanket and handkerchiefs")
        pass # Add in Sprint 8

# ---------- Task 5 ----------/
    def test_order_2_ice_creams(self):
        print("function created for order 2 ice creams")
        for i in range(2):
            pass # Add in Sprint 8

    def test_car_search_model_appears(self):
        print("function created for car search model appears")
        pass # Add in Sprint 8