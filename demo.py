import requests

def format_string(input_string):
    # Split the input string into parts
    parts = input_string.split()
    # Join the parts with '/' for the first part and format the rest
    formatted_string = f"{parts[0]}/" + '%20'.join(parts[1:])
    return formatted_string

# Example usage
def product_data(input_str):
		#input_str = "samsung galaxy s20 5g"
		output = format_string(input_str)
		url = f"https://mobile-phone-specs-database.p.rapidapi.com/gsm/get-specifications-by-brandname-modelname/{output}"
		headers = {
			"x-rapidapi-key": "67b4652ea8mshe0bf39cbbdf4b1dp15ca3ajsnc52c70074555",
			"x-rapidapi-host": "mobile-phone-specs-database.p.rapidapi.com"
		}
		response = requests.get(url, headers=headers)
		print(response.json())
		return (response.json())



