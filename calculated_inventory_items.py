import requests
from endpoints import BASE_URL

def update_calculated_inventory_item(calculated_inventory_item_uuid,header,payload):
    url = f'{BASE_URL}/v2/admin/calculated-inventory-items/{calculated_inventory_item_uuid}'

    response = requests.patch(url,headers=header,data=payload)

    if response.status_code == 200:
        print(f'{calculated_inventory_item_uuid} Updated')
        return True
    else:
        print(f'{calculated_inventory_item_uuid} Update Failed')
        return False