import os
from django.core.management.base import BaseCommand
from django.core.files import File
from reviews.models import ClientReview
from core.models import Sprite
from PIL import Image


class Command(BaseCommand):
    help = 'Populates the database with the initial reviews'

    def handle(self, *args, **options):
        ClientReview.objects.all().delete()
        for review in self.get_reviews():
            if 'image' in review:
                image_file = open(os.getcwd() + '/reviews/management/commands/' + review.get('image'), 'r')
                image_file.seek(0)
		# import ipdb; ipdb.set_trace()
	        # test = ClientReview.objects.create(name=review.get('author'), text=review.get('text'), thumbnail=File(image_file))
	        test = ClientReview.objects.create(name=review.get('author'), text=review.get('text'))
		test.thumbnail.name = 'reviews/management/commands/' + review.get('image')
		test.save()
            else:
                ClientReview.objects.create(name=review.get('author'), text=review.get('text'))
        review_sprite = Sprite.objects.get(name='reviews')
        review_sprite.generate()


    def get_reviews(self):
        return [
            {
                "text": "It is hard to finds words that are strong enough to express my thanks to you for yesterday. Every bride wants to look their best for their groom on their wedding day. Not only did you make me look beautiful, Orly, but I felt it! You are so professional and yet so personable, attentive and the way you listen to what your clients want is priceless. From the bottom of my heart, thank you",
                "author": "Amy C.",
                "image": "amy.jpg",
            },
            {
                "text": "Orly did an amazing job, she was a pleasure to have around, and provided a much needed calmness to a very hectic day! Orly was incredibly flexible and managed to make a group of very fussy ladies extremely happy with their make up, accommodating to each persons personal style.",
                "author": "Baily",
                "image": "baily.jpg",
            },
            {
                "text": "From the first phone call to arrange a makeup trial, I found a comfort in talk...ing to Orly. Orly is amazing. During the whole process she was completely supportive and rock and rolled with every request ensuring mine and my families comfort. Throughout numerous trials and ingredient discussions, Orly was professional and accommodating to ensure our satisfaction. Equally as amazing as her being so great to work with, is her makeup. As I am someone with little understanding of makeup, Orly was able to transform me into exactly what I had envisioned. She understands your face and makes you feel the way you should on your wedding day. I am very grateful I was given her number and truly honoured to be able to call her my good friend. I highly recommend her to anyone in need of an amazing makeup artist",
                "author": "Sondra",
                "image": "sondra.jpg",
            },
            {
                "text": "Hi Orly,<br>I was absolutely thrilled to have my makeup done by you. I am so glad that you recommended me to wear false eyelashes because it really complimented my whole face. My eyes popped as you said it would and so many people told me that my makeup was beautifully done. I cried, smiled, laughed and my makeup lasted the whole night.<br>You are very professional, accommodating and you truly exceeded my expectations with your fabulous work.<br>I would definitely recommend you to all my friends and families.",
                "author": "Judy",
            },
            {
                "text": "All of the girls loved how beatiful you both made us. My make-up looked flawless all night : ) Thank you so very much for making my big day a memorable one, you are very professional and I really appreciate that. I will send you pictures as soon as I get them, do you have a facebook page?<br>P.S. THANK YOU for telling me about Shai too did a beatiful job. Great team of make-up and hair designers.<br>From the bottom of my heart I thank you and I will not hesitate to contact you for any future events.",
                "author": "Haizel",
                "image": "haizel.png",
            },
            {
                "text": "Orly was great! She was very friendly and professional at the same time. She did my bridesmaids makeup my moms and my self. The products she used where really good they are water based so you dont get that heavy feeling when its on your skin and it stayed on all day and night!! I would recommend any bride to give orly a call. She provides a great service for a great price :)",
            },
            {
                "text": "Orly was really great! Doesn't overcharge like some of the others out there, punctual, professional and good at what she does. Everybody looked great. Her accompanying hair associate (Shai Farzaneh) is simply fabulous with hair and they make a great team (though Shai is a tad bit disorganized in an artsy way).",
                "author": "Naveli",
            },
            {
                "text": "Orly does wonderful work, I felt absolutly beautiful on my wedding day! She was also very quick to respond to any questions I had leading up to the big day, as well as always being very friendly and personal. ",
            },
            {
                "text": "Orly was fantastic! She was always so responsive to emails, accomodating with our timing day of, and so open to what each girl was looking for with make-up. She was open to suggestions and had such great ideas, and a lovely and relaxed person to spend time with on our wedding day! Incredible value as well. Highly recommend working with Orly any time!",
            },
            {
                "text": "Orly was amazing to work with and did a crazy awesome job! I used her for my engagement photos, bridal shower and on the day of my wedding she did the make-up for me and my bridal party. I have recommended her to my friends and will definitely use her again.",
            },
            {
                "text": "I came across Orly by a recommendation made by a friend. I found Orly's website and decided to give her a call. She was very professional and gave me all the information I needed. Orly and I scheduled a makeup trial the day of my bridal shower. Orly asked me questions based on my daily makeup use. She went for a very natural look and it looked fantastic. My guests absolutely loved it and I received an abundance of compliments. Right from the trial, I knew that I had to finalize my booking with her for the day of the wedding. On the big day, she was very punctual and same with her assistant, Vise. These two ladies worked their magic and all of us looked incredible. We received a lot of compliments and we thought that the two of them were very friendly and personable.<br>I have already recommended Orly to a friend who also used Orly's services the day of her wedding. I will continue to recommend Orly to people that I know that will wed or have a special event in the near future. Thank you both ever so much for your talented work!!!",
                "author": "Tiffany R.",
            },
            {
                "text": "Orly did the make up for myself and my bridal party for my wedding and did an amazing job. She was so sweet and very professional. She started and finished exactly on schedule while also taking her time. Everyone looked so beautiful and very natural and we received so many compliments on all the make up throughout the night. I would definitely reccomend Orly for make up for any occassion!",
                "author": "Rebecca",
            },
            {
                "text": "Orly is an exceptional make up artist! She is extremely friendly and amazing at what she does! My mom does not wear make up and was a little uncomfortable with the idea....once orly did her make up not only did my mom look amazing she wad amazed at how great the make was and how light it felt. I had compliments all night. Any future events I need make up done there is no doubt in my mind I would call or recommend orly. I cannot thank her enough for making me look and feel like a princess on my wedding day!",
                "author": "Steph",
                "image": "steph.jpg",
            },
            {
                "text": "From the start, Orly was very professional and responsive. She came to the venue and completed the make-up for seven people quickly but didn't scrimpt on quality! My bridesmaids, my mom & mother-in-law were all very happy with her work. Orly even went to my mother-in-law's hotel room to make it more comfortable for her.<br>I would highly recommend Orly. She's personable and is able to make everyone feel at ease. She in very talented and everyone's make-up lasted until the end (even with a lot of dancing!). Thank you Orly for making me look & feel beautiful on my wedding day.",
                "author": "Laura H",
                "image": "laura.jpg",
            },
            {
                "text": "Orly was very professional but still friendly and made me comfortable about having her do my makeup on my wedding day. She did a fantastic job and all of my bridesmaids, along with my mom and aunt were thrilled with her work and we all received compliments on our makeup all day long. Not only did she come to my house on time and with all of her products, but she was super friendly, she did a great job, she put everyone at ease, and she worked in a timely manner. I would highly recommend Orly to other brides, she was my favourite vendor and I know my family and friends will be using her for future weddings!",
                "author": "Stephanie",
                "image": "stephanie.jpg",
            },
            {
                "text": "Orly provide make-up services for my Bridesmaids and I on December 31, 2011. She also did my make-up for my engagement photo session earlier in the year. My make-up looked fantastic and I look forward to recommending her services to friends and family!",
                "author": "Ashley E.",
            },
            {
                "text": "Orly was fantastic and I couldn't be happier with the service she provided for my bridesmaids, mother and I. From the moment I contacted her she was professional and informative. She would respond quickly to any questions I had. My bridesmaids and I are pretty flexible and easy going, so it was easy for Orly to work with us. She always made sure we felt comfortable and if we required a change she was more than happy to modify our make-up. I didn't have to touch up my make up except my lipstick. The value I found was great for trial and day of wedding compared to some prices I came across.<br>I couldn't be happier picking Orly as my make-up artist. My wedding pictures are gorgeous.<br>Thank you Orly!",
                "author": "Sandy",
                "image": "sandy.jpg",
            },
            {
                "text": "Orly is amazing!! Your makeup skills are out of this world. You helped make my day special and for that I am so greatful!!<br>THANKS YOU!!! You are fantastic!!!!",
                "author": "Charlene",
            },
            {
                "text": "Orly was extremely professional and easy to work with. If you're looking for a flawless lasting look for your special event or wedding, she's definitely worth the price. She comes on time, works quickly and efficiently and I was extremely happy with the results. She did my makeup for my wedding and also my mom's makeup. We have nothing but the best to say about working with her.",
            },
            {
                "text": "Orly was amazing and really did a spectacular job on our makeup. I've hired her three times now and have confidently recommended her to other brides as well. She's wonderful and she made a recommendation for an equally great hair stylist as well. We were thrilled and it showed in the pictures! :)",
                "author": "Genevieve",
                "image": "genevieve.jpg",
            },
            {
                "text": "Hi Orly,<br>I just wanted to send a quick thank you for taking such good care of all of us on Saturday. We were all thrilled with how our makeup came out, and we got so many compliments. The makeup looked fresh all night long! I know we were a pretty large group to handle, so we really appreciate all your work. You were absolutely wonderful and I will for sure recommend you to anyone in need of a makeup artist!<br>Thanks again",
                "author": "Kelley",
                "image": "kelley.jpg",
            },
            {
                "text": "I was the kind of bride who didn't care much for backdrops, center pieces, overlays, etc. The most important thing to me was that I look my best on my wedding day. Now, some make up artists take that as meaning that I want to not look like myself. No. I wanted to look like the more enhanced version of myself. I didn't want to look in the mirror and not recognize the face staring back at me. <br>During my make up trial with Orly, the one thing that struck me different from all of the other make up artists was that when you told her you wanted to change something here, or change something there, she was totally cool with it. After the make up trial, even though I wasn't 100% with the make up (I still had some more research to do on what I even wanted!), I was definitely 100% on the make up artist. <br>Up until the night before the wedding, I was emailing Orly pictures and sending her messages. She never got upset. Also, the night before the wedding, Orly messaged me to say how she was excited for the big day. Who else does that!? <br>Come the next day, I was so nervous, but not Orly. After getting my make up done, I looked in the mirror and I looked beautiful! Everything that I told her that I wanted did not go in one ear and out the other. It was perfect! For those of you who do want a more natural, matte look, that is what I did and WOW. <br>I know I seem a little too excited about this review, but I truly do believe that in order to have a successful and RELAXED wedding day, you have to trust the people you're putting your face in. Orly is kind, sweet, and works magic with make up. <br>P.S. Orly also did my mom's make up and she looked UNBELIEVABLE. <br>P.P.S. My mom and I were going for different looks, and each looked different, but still amazing. Says something about a make up artist who doesn't have one style. <br>Thanks Orly!",
                "author": "Kelley",
                "image": "yael.jpg",
            },
            {
                "text": "I usually do my own makeup. I was never happy after having my makeup professionally applied, always feeling as though I was walking away not looking at all like myself. I am very particular about having perfectly drawn eyeliner, long lashes, natural looking and feeling foundation, etc. Going to a friend made me even more skeptical at first, what if I wasn't happy? <br>I took a chance and went to see Orly for a trial. When her work was complete, I was totally blown away by my transformation -- Orly did exactly as I hoped: natural makeup, not too heavy and she made my eyes look amazing! Perfect liner and perfect lashes! . <br>Going with Orly was one of the best decisions I made throughout the entire process of planning a wedding. Her brilliance came through fully a few months after the weddi...ng wen I saw the prints from our photographer. <br>Not only is she incredibly talented she is a wonderful person with a genuine heart and will go out of her way to make sure you are happy. <br>If you are a bride searching for a stunning makeup artist , you found her. Orly will listen closely to your requests, you will be truly amazed by the outcome. <br>Thank you Orly for making my wedding day that much more perfect!",
                "author": "Rachel",
                "image": "rachel.jpg",
            },
            {
                "text": "I cannot say enough positive things about Orly. After having had her do my makeup as a bridesmaid at my sister-in-law's wedding, I immediately knew she would be the right person to do my wedding make-up. If I could give her six stars on flexibility I would - she will work with whatever make-up you want (if you have your own) and use her own wide array of top-quality products if not. Orly also make thoughtful recommendations about anything from colours to brands to what looks the best in photos. She was also able to work on a truncated timeline, after the venue staff opened up late, and still get everyone done on time. The makeup lasted throughout the entire day and the application was not uncomfortable. We all looked great, thank-you Orly!",
                "author": "Felicia",
            },
            {
                "text": "After having a few bad experiences with makeup artists I had found online for my wedding, I came across Orly's website and had a different feeling about her. I contacted her and immediately she responded to my inquiry. From day one, she was friendly, reliable and professional. I pursued a trial with her and after that, I was sold. On the day of my wedding she came as her usual self; prepared, on time and friendly as ever, as we all had some serious nerves going on for the big day. We needed her a little longer for extra video footage and she was very accommodating and flexible in staying that extra bit of time, even though she had another wedding scheduled for later. I would highly recommend her to brides and others alike who want to be beautified for a day. Thanks again Orly!",
                "author": "Jennifer",
                "image": "jenn p.png",
            },
        ]
