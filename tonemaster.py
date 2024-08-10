def get_skin_type():
    print("What is your skin type?")
    print("1. Oily")
    print("2. Dry")
    print("3. Combination")
    print("4. Sensitive")
    choice = input("Enter the number corresponding to your skin type: ")
    skin_types = {
        "1": "Oily",
        "2": "Dry",
        "3": "Combination",
        "4": "Sensitive"
    }
    return skin_types.get(choice, "Unknown")

def get_skin_concerns():
    print("What are your primary skin concerns?")
    print("1. Acne")
    print("2. Aging")
    print("3. Hyperpigmentation")
    print("4. Redness")
    print("5. Uneven texture")
    concerns = input("Enter the numbers corresponding to your concerns, separated by commas: ")
    concerns_list = [concern.strip() for concern in concerns.split(',')]
    concerns_map = {
        "1": "Acne",
        "2": "Aging",
        "3": "Hyperpigmentation",
        "4": "Redness",
        "5": "Uneven texture"
    }
    return [concerns_map.get(c, "Unknown") for c in concerns_list]

def suggest_routine(skin_type, concerns):
    print("\nBased on your inputs, here is a suggested skincare routine:")
    print(f"Skin Type: {skin_type}")
    print("Routine:")
    
    # Cleansers
    if skin_type == "Oily":
        print("- Use a foaming cleanser to control excess oil.")
    elif skin_type == "Dry":
        print("- Use a hydrating or creamy cleanser to avoid stripping moisture.")
    elif skin_type == "Combination":
        print("- Use a gentle, balanced cleanser.")
    elif skin_type == "Sensitive":
        print("- Use a mild, fragrance-free cleanser.")
    
    # Moisturizers
    if skin_type == "Oily":
        print("- Use a lightweight, oil-free moisturizer.")
    elif skin_type == "Dry":
        print("- Use a rich, hydrating moisturizer.")
    elif skin_type == "Combination":
        print("- Use a moisturizer suited for combination skin.")
    elif skin_type == "Sensitive":
        print("- Use a fragrance-free, hypoallergenic moisturizer.")
    
    # Treatments based on concerns
    for concern in concerns:
        if concern == "Acne":
            print("- Consider using products with salicylic acid or benzoyl peroxide.")
        elif concern == "Aging":
            print("- Look for products with retinoids or peptides.")
        elif concern == "Hyperpigmentation":
            print("- Use products with vitamin C or niacinamide.")
        elif concern == "Redness":
            print("- Use products with soothing ingredients like aloe or chamomile.")
        elif concern == "Uneven texture":
            print("- Consider exfoliating with chemical exfoliants like AHAs or BHAs.")
    
    print("\nRemember to consult with your dermatologist for personalized advice.")

def main():
    print("Welcome to the Skincare Routine Suggestion Program!")
    skin_type = get_skin_type()
    concerns = get_skin_concerns()
    suggest_routine(skin_type, concerns)

if __name__ == "__main__":
    main()
