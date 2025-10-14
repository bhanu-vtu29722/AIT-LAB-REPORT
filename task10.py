facts = [
 "john_is_cold.", # john is cold
 "raining.", # it is raining
 "john_Forgot_His_Raincoat.", # john forgot his raincoat
 "fred_lost_his_car_keys.", # fred lost his car keys
 "peter_footballer." # peter plays football
]

def verify_fact(fact):

         fact = fact.rstrip(".")
         # Perform some logic to verify the fact
         if fact == "john_Forgot_His_Raincoat":
               return True
         elif fact == "raining":
               return True
         elif fact == "foggy":
              return True
         elif fact == "Cloudy":
              return False # Assume it's n
         else:
            return False

for fact in facts:
     if verify_fact(fact):
          print(f"{fact} - Yes")
     else:
           print(f"{fact} - No")
