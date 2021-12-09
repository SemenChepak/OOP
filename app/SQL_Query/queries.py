QUERIES = {'all': f"SELECT * from people" \
                f" left join cards on people.customer_id = cards.holder_id " \
                f"left join transactions on cards.card_no = transactions.card_number",

         'clients': "SELECT * from people",
         'cards': "SELECT * from cards",
         'transactions': "SELECT * from transactions "}
