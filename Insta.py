#InstaPy Files
from instapy import InstaPy
from instapy import smart_run

class Insta:
    def __init__(self, username='dave.x_x', password='hood@ins.com', headless=True):
        self.session = InstaPy(
                username=username,
                password=password,
                headless_browser=headless)
        self.username=username
        self.password=password
        self.headless=headless
    pic_comments=[
            'This picture is astounding.', 
            'This is the best i"ve seen until now.',
            'This picture is lit!!',
            'Hot!',
            'That"s a killer pic bro',
            'Keep shining.',
            'Boss!!',
            'You inspire me!',
            'Million-dollar pic',
            'Looking like a star.',
            'Awesome pictures bro.',
            'Your charm is irresistible!',
            'You are like coming home!',
            'This picture is better than better.',
            'Totally contemporary & aesthetic look',
            'You are a lovely ness.']
    vid_comments=[
            'Crazzyyy', 
            "What's going on here fam", 
            'A lot is going on here', 
            u'Tf', 
            u'Guyyy', 
            u'🔥❤️', 
            'slime',
            'beautiful mess',
            u'Charmed😌']
    
    
    
    def settings(self):
        self.session.login()
        self.session.set_quota_supervisor(
                enabled=True,
                sleep_after=[
                    "likes_d",
                    "comments_d",
                    "follows_d",
                    "unfollows_d",
                    "server_calls_d"],
                sleepyhead=True,
                stochastic_flow=True,
                notify_me=True,
                peak_likes_hourly=60,
                peak_likes_daily=1440,
                peak_comments_hourly=60,
                peak_comments_daily=1440,
                peak_follows_hourly=30,
                peak_follows_daily=720,
                peak_unfollows_hourly=60,
                peak_unfollows_daily=1440,
                peak_server_calls_hourly=None,
                peak_server_calls_daily=None)
        self.session.set_skip_users(
                skip_private=True,
                private_percentage=100,
                skip_no_profile_pic=True,
                no_profile_pic_percentage=100,
                skip_business=False,
                skip_non_business=False,
                business_percentage=100)
        self.session.set_delimit_liking(
                enabled=True,
                max_likes=None,
                min_likes=10)
        self.session.set_delimit_commenting(
                enabled=True,
                max_comments=None,
                min_comments=2)
        self.session.set_relationship_bounds(
                enabled=True,
                potency_ratio=1.5,
                delimit_by_numbers=True,
                max_followers=None,
                max_following=None,
                min_followers=2000,
                min_following=None,
                min_posts=5,
                max_posts=None)
        self.session.set_action_delays(
                enabled=True,
                like=2,
                comment=2,
                follow=5,
                unfollow=5,
                story=5)
        self.session.set_mandatory_language(
                enabled=True, 
                character_set=['LATIN'])
            
    def follow(self):
        self.session.set_comments(
            self.pic_comments,
            media='Photo')
        self.session.set_comments(
            self.vid_comments,
            media='Video')
        self.session.set_do_comment(
            enabled=True,
            percentage=50)
        self.session.set_do_follow(
            enabled=True,
            percentage=100,
            times=1)
        self.session.set_user_interact(
            amount=5,
            randomize=False,
            percentage=100)
        self.session.follow_likers(
            ['wizkid' , 'davido', 'burnaboygram', 'selenagomez', 'iamcardib',
             'kimkardashian', 'thedrake', 'kingjames', 'kevinhart4real', 'therock'], 
            photos_grab_amount = 2, 
            follow_likers_per_photo = 5, 
            randomize=True, 
            sleep_delay=60, 
            interact=True)
        
    def gain(self):
        self.session.follow_user_following(
            ['selenagomez', 'iamcardib', 'kimkardashian', 'thedrake', 'kingjames', 'kevinhart4real', 'therock'], 
            amount=20, 
            randomize=True)
        
        
    def unfollow(self):
        nonfollowers=self.session.grab_following(
            username="dave.x_x", 
            amount="full", 
            live_match=False, 
            store_locally=False)
        self.session.unfollow_users( 
            custom_list_enabled=True, 
            custom_list=nonfollowers,
            custom_list_param="all", 
            style="RANDOM", 
            sleep_delay=60)
            
    def scroll(self):
        self.session.set_do_comment(
                enabled=True,
                percentage=50)
        self.session.set_comments(
                self.pic_comments,
                media='Photo')
        self.session.set_user_interact(
                amount=3,
                randomize=True,
                percentage=50)
        self.session.like_by_feed(
            amount=100, 
            randomize=True, 
            unfollow=True, 
            interact=True)
        
    def stories(self):
        following = self.session.grab_following(
            username="dave.x_x", 
            amount="full", 
            live_match=True, 
            store_locally=False)
        self.session.set_do_story(
            enabled = True, 
            percentage = 70, 
            simulate = True)
        self.session.interact_by_users(following, amount=0, randomize=True, media='Photo')

        
    def end(self):
        self.session.end()
