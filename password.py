password = input("What password would you like to use?")
confirmPassword = input("Please retype your password?")

if password != confirmPassword:
    print("🚫 both passwords need to match")
elif len(password) < 8:
    input("🚫 Password must be at least 8 characters long")
else:
    print("✅ snap!")
