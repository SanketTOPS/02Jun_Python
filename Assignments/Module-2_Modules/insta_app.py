import instaloader

instaID=input("Enter any instagram's ID:")

insta=instaloader.Instaloader()
insta.download_profile(instaID)
print("Download Successfully!")