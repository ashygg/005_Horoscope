import random

intro = "Hello and welcome! If you enter your date of birth (month/day  i.e May 19), I'll provide you with a horoscope reading!"
print(intro)

birth_month = input("What is your birth month? ").lower()
birth_date = int(input("What is your birth day? "))

yr_months = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "november", "december")
if not (birth_month in yr_months):
    print("Sorry! Please check your spelling!")

if (birth_month=="march" and birth_date>=21) or (birth_month=="april" and birth_date<=19):
    star_sign = "Aries"
elif (birth_month=="april" and birth_date >=20) or (birth_month=="may" and birth_date<=20):
    star_sign = "Taurus"
elif (birth_month=="may" and birth_date>=21) or (birth_month=="june" and birth_date<=20):
    star_sign = "Gemini"
elif (birth_month=="june" and birth_date>=21) or (birth_month=="july" and birth_date<=22):
    star_sign = "Cancer"
elif (birth_month=="july" and birth_date>=23) or (birth_month=="august" and birth_date<=22):
    star_sign = "Leo"
elif (birth_month=="august" and birth_date>=23) or (birth_month=="september" and birth_date<=22):
    star_sign = "Virgo"
elif (birth_month=="september" and birth_date>=23) or (birth_month=="october" and birth_date<=22):
    star_sign = "Libra"
elif (birth_month=="october" and birth_date>=23) or (birth_month=="november" and birth_date<=21):
    star_sign = "Scorpio"
elif (birth_month=="november" and birth_date>=22) or (birth_month=="december" and birth_date<=21):
    star_sign = "Sagittarius"
elif (birth_month=="december" and birth_date>=22) or (birth_month=="january" and birth_date<=19):
    star_sign = "Capricorn"
elif (birth_month=="january" and birth_date>=20) or (birth_month=="february" and birth_date<=18):
    star_sign = "Aquarius"
elif (birth_month=="february" and birth_date>=19) or (birth_month=="march" and birth_date<=20):
    star_sign = "Pisces"
print("Your sign is "+star_sign,"! Here is a 2023 horoscope for you: ")

aries_horoscope = [
    "Although there will likely be hard times to test you, you will come out stronger in the end.",
    "You have the potential for a lovely romance this year.",
    "In terms of academics, you should go in with a positive mindset! You are more likely to find the success that you want!",
    "Be aware of your health this year! Try to keep up with healthy habits with food, sleep, and exercise.",
    "Be mindful of your finances. Although there may be some instability, if you maintain good investments and don't overspend, you will be in a good position.",
    "You may find changes at your workplace this year. There may be challenges at the beginning of the year, but you may find achievements near the end."
]

if star_sign == "Aries":
    for i in range(1):
        aries_prediction = random.choice(aries_horoscope)
        print(aries_prediction)

taurus_horoscope = [
    "Go into challenging scenarios with a positive attitude and you will obtain positive outcomes.",
    "If you are looking into marriage, this year may bring romantic success.",
    "Your depression/anxiety may cause you mental stress this year due to things working out of your favor, but meditation may help.",
    "You will have good luck with money this year. Have a prior plan for your finances and expenditures.",
    "Along with gaining new skills and desires, you will find success.",
    "If you are looking into admission into higher education, you may find success in a foreign institute."
]

if star_sign == "Taurus":
    for i in range(1):
        taurus_prediction = random.choice(taurus_horoscope)
        print(taurus_prediction)

gemini_horoscope = [
    "Be cautious in making new friends this year.",
    "Take care of potential romantic relationships, you may achieve something new in your life.",
    "Keeping a good routine this year will benefit you greatly.",
    "There will be multiple ways for you to gain financial benefit, use caution.",
    "You will have a great year and find new platforms to shine on.",
    "Use patience and perseverance for your studies and your efforts will pay off."
]

if star_sign == "Gemini":
    for i in range(1):
        gemini_prediction = random.choice(gemini_horoscope)
        print(gemini_prediction)

cancer_horoscope = [
    "Let love take it's course naturally and you'll find feelings of abundance.",
    "Take care of your health and be aware of any issues you may face. See a doctor from time to time.",
    "With your efforts, you will have potential to gain strong finances.",
    "Keep focus on your goals and take your time. Taking it slowly and paying attention to details will fetch better results."
]

if star_sign == "Cancer":
    for i in range(1):
        cancer_prediction = random.choice(cancer_horoscope)
        print(cancer_prediction)

leo_horoscope = [
    "Place full trust in your abilities and go full throttle, your success will follow you.",
    "Even if you experience tension or a mental breakdown, keep in mind that this year is the year you discover more about yourself.",
    "Avoid negative thoughts and avoid situations that make you feel negatively.",
    "You will experience self-realization this year and find what you like and believe in."
]

if star_sign == "Leo":
    for i in range(1):
        leo_prediction = random.choice(leo_horoscope)
        print(leo_prediction)

virgo_horoscope = [
    "Working hard and using your determination will bring about your desired successes.",
    "You may experience a change in your outlook this year, but it will bring about happiness and prosperity.",
    "Not overstressing and consuming a healthy, balanced diet will allow you to enjoy good health.",
    "You may experience financial loss this year. It may help to seek a financial advisor.",
    "You should resolve differences you find between yourself and others this year."
]

if star_sign == "Virgo":
    for i in range(1):
        virgo_prediction = random.choice(virgo_horoscope)
        print(virgo_prediction)

libra_horoscope = [
    "In terms of studies, your efforts will pay off and you will receive good results.",
    "You will experience tremendous personal growth this year. Keeping friends and family close to you will improve your life.",
    "Be wary of your health this year. If not, you may experience changes in your happiness.",
    "Creating a plan for your finances will create a favourable situation for you.",
    "Being patient with your work will bring new opportunities."
]

if star_sign == "Libra":
    for i in range(1):
        libra_prediction = random.choice(libra_horoscope)
        print(libra_prediction)

scorpio_horoscope = [
    "Appreciating and accepting others will bring long-lasting ties. Avoid toxic relationships.",
    "If you had bad health previous years, you may find ease this year. Be mindful of your mental health and wellness.",
    "It is recommended for you to think wisely and make decisions which might balance your expenses.",
    "Career predictions say that great opportunities are waiting for you.",
    "You are likely to focus more on your studies due to which your performance seems to also improve gradually."
]

if star_sign == "Scorpio":
    for i in range(1):
        scorpio_prediction = random.choice(scorpio_horoscope)
        print(scorpio_prediction)

sagittarius_horoscope = [
    "Remember to put in your best so that you might achieve desired results. Everything is possible with hard work and great efforts.",
    "Have patience and control your anger in every situation. Avoid unnecessary arguments.",
    "Try new things with your partner to create beautiful moments. Do not include anybody else in your connection.",
    "You might need to spend more on your health and this might build your concerns and nervousness as well.",
    "Financial prosperity seems to be there. Take precautions on how you use the money so that you might handle it efficiently.",
    "Your overall subject wise performance might greatly improve such that you might be appreciated by your mentors and friends."
]

if star_sign == "Sagittarius":
    for i in range(1):
        sagittarius_prediction = random.choice(sagittarius_horoscope)
        print(sagittarius_prediction)

capricorn_horoscope = [
    "This year will be exciting and that your efforts will be dutifully rewarded. You'll make new friends and experience positive life-changing progress in many areas.",
    "But if you are not taking care of your health with a proper routine, then it may go down. So it is advisable to eat quality food to stay away from undesirable illnesses.",
    "It might be a good time to make important financial decisions. No doubt your finances seem to support you but expert advice is really important if you are planning for any kind of investment.",
    "Stick to your plan and pursue your dreams with dedication."
]

if star_sign == "Capricorn":
    for i in range(1):
        capricorn_prediction = random.choice(capricorn_horoscope)
        print(capricorn_prediction)

aquarius_horoscope = [
    "Negligence or laziness might lead you to repents. Continue working hard for success.",
    "2023 will bring lots of amazing experiences. You might come up with some changes in life and you have to work hard to achieve certain goals in your life.",
    "Expenses need to be cut down and proper financial management needs to be looked upon.",
    "This is the time to regroup your energies and try hard to achieve your goals."
]

if star_sign == "Aquarius":
    for i in range(1):
        aquarius_prediction = random.choice(aquarius_horoscope)
        print(aquarius_prediction)

pisces_horoscope = [
    "You might perform well but, at times your overconfidence might make you careless and hence you might not be able to prepare or concentrate well in studies in the beginning of this year.",
    "Keep calm, look after yourself and move ahead to achieve your goals.",
    "You might require taking extra consideration of your health. In order to attain good health, try to adopt a good eating routine and workouts on a daily basis.",
    "Be careful not to take your connection for granted. A carefree attitude and self-consciousness are more likely to result in some disturbances."
]

if star_sign == "Pisces":
    for i in range(1):
        pisces_prediction = random.choice(pisces_horoscope)
        print(pisces_prediction)
