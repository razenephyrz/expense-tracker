from schemas.transaction import TransactionCreate, TransactionType

def main():
    t = TransactionCreate(category_name='  MAKANAN ', amount=10000, type=TransactionType.expense)
    print(t)

if __name__ == "__main__":
    main()
