# final_price = int(input()) * 7.61
# print(f'The final price is: {final_price - (0.18 * final_price)} lv.')
# print(f'The discount is: {0.18 * final_price:.2f} lv.')

sqr_m = float(input())
final_price = sqr_m * 7.61
discount = 0.18 * final_price
final_price2 = final_price - discount
print(f'The final price is: {final_price2:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')
