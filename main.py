def main():
   ##################################################
   # Comlete your code here
   ##################################################
    #original_price = int(200)
      
#     original_price = int('Enter your price')
    original_price = int(input('Enter your price'))

    
    rate = int(input('Enter your rate'))
   
    discount_amount = original_price * rate / 100
    print(original_price)
    print(discount_amount)
    print(original_price - discount_amount)
    
    pass


if __name__ == '__main__':
    main()
