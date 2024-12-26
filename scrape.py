import requests
from bs4 import BeautifulSoup
import requests , re , json , time , random
from datetime import datetime
class ReviewScrape:
    def __init__(self):
        version = random.randint(129,132)
        self.headers  = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'dpr': '1',
            'priority': 'u=0, i',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"19.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36 Edg/{version}.0.0.0',
            'viewport-width': '833',
        }
        self.client = requests.Session()
        self.client.headers.update(self.headers)
        self.breakout = 0
        self.c_user = ""
    def run(self , URLs : str):
        self.orderId = 1
        self.reviews = []
        self.URLs = URLs
        self.cursor = '{\\"in_progresscursor_type\\":\\"online\\",\\"local_rec_pattern_cursor\\":\\"\\",\\"rating_cursor\\":\\"\\",\\"offline_offset\\":-1}"}'
        self.html_and_cursor()
        while self.cursor:
            # self.orderId += 1
            self.client.headers.update({'x-asbd-id': f'{random.randint(129477,129477)}'})
            self.parse_json_data()

        if self.reviews != []:
            self.reviews = self.reviews[:-1]
            return self.reviews
        #     with open('data_.json' , 'w', encoding='utf-8') as f:
        #         json.dump(self.reviews, f , ensure_ascii=False , indent=4)
        # print(json.dumps(self.reviews , ensure_ascii=False , indent=4))
    def html_and_cursor(self):
        reponse = self.client.get(self.URLs)
        if reponse.status_code == 200:
            self.cursor = re.search(r'\\"local_rec_pattern_cursor\\":\\"(.*?)\\",\\' , reponse.text).group(1)
            self.id = re.search(r'content="fb://profile/(.*?)"' , reponse.text).group(1)

            soup = BeautifulSoup(reponse.text, 'html.parser')
            # Get To Script Json
            script_tag = soup.find_all('script', {'type': 'application/json', 'data-sjs': True})
            for script in script_tag:
                if re.search('color_ranges', script.text) and re.search('copyright_violation_header', script.text):
                    # Phân tích JSON từ script tag
                    json_data = json.loads(script.text)["require"][0][3][0]["__bbox"]["require"]

                    # Xử lý từng phần tử trong JSON
                    for data_item in json_data:
                        post_info = self.parse_html_data(data_item)
                        if post_info:
                            self.reviews.append(post_info)
                            self.orderId += 1

    def parse_json_data(self ):
        data  = {
        'av': self.c_user,
        '__aaid': '0',
        '__user': self.c_user,
        '__a': '1',
        '__req': 'r',
        '__hs': '20082.HYP:comet_pkg.2.1.0.2.1',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1019074588',
        '__s': 'xpjjgm:milg84:kw6df5',
        '__hsi': '7452315291467231561',
        '__dyn': '7xeXxaU5a5Q1ryaxG4Vp41twWwIxu13wFwhUngS3q2ibwNwnof8boG0x8bo6u3y4o2Gwfi0LVEtwMw6ywIK1Rwwwqo462mcwfG12wOx62G5Usw9m1YwBgK7o6C0Mo4G1hx-3m1mzXw8W58jwGzE8FU5e3ym2SU4i5oe8464-5pUfEe88o4Wm7-2K0SEuwLKq2-azqwaW223908O3216xi4UK2K364UrwFg2fwxyo566k1FwgUjwOwWzUfHDzUiwRK6E4-mEbUaUaE2Tw',
        '__csr': 'gkg8v138wDkQIaNq6MBtTNmDqtHWEhi9dnEJnmn4Ohn9ZdbtlYx9eAl8BWFHZRV4nDybFrJplmjkHyfucKWzozWLhpEOmKKGgK9yqyvBx2fiQHzbzVeUnypfUhVWABVFXBuFGUnzogy8Obx29G4FGzUOeBBx52oGGwBUK4Eox29VU9A2a2C6UnzESdK16wgUnwkUlgpxS2W9y888d85u6U9VE2lw-wPhE31wgE2qwWwaW1mw38Evw24awdW0rW1dw1QK8w05hnw0y3g1Co2Qwbm0Hk8w2vU1P87K0dlw1ei02ju0cFw09J607E8',
        '__comet_req': '15',
        'jazoest': '25271',
        'lsd': 'V7lmAeDsoiLiI3fc119D-9',
        '__spin_r': '1019074588',
        '__spin_b': 'trunk',
        '__spin_t': '1735127366',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'ProfileCometReviewsFeedRefetchQuery',
        'variables': '{"count":1000,"cursor":"{\\"in_progresscursor_type\\":\\"online\\",\\"local_rec_pattern_cursor\\":\\"'+self.cursor+'\\",\\"rating_cursor\\":\\"\\",\\"offline_offset\\":-1}","feedLocation":"PAGE_SURFACE_RECOMMENDATIONS","feedbackSource":0,"focusCommentID":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"timeline","scale":1,"useDefaultActor":false,"id":"' +self.id+ '","__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":false,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider":500,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":false}',
        'server_timestamps': 'true',
        'doc_id': '8280791252021294',
    }
        

        response = self.client.post('https://www.facebook.com/api/graphql/', data=data)
        # print(response.text)
        for line in response.text.split('\n'):
            data = json.loads(line).get('data',{})
            self.cursor = None
            
            try:
                data_node = data['node']['ratings_list_feed_units']['reviews_feed']['edges'][0]['node']
            except KeyError:
                try:
                    page_info = data['page_info']
                    has_next_page = page_info.get('has_next_page', False)
                    self.cursor = json.loads(page_info['end_cursor'])['local_rec_pattern_cursor']
                except KeyError:
                    data_node = data.get('node', {})


            if self.cursor:
                break

            # Posts 
            try:
                author_name = data_node['comet_sections']['content']['story']['actors'][0]['name']
            except:
                # Không vó name
                author_name = ""

            try:
                post_content = data_node['comet_sections']['content']['story']['message']['text']
            except:
                try:
                    post_content = data_node['comet_sections']['content']['story']['attachments'][0]['styles']['attachment']['tags'][0]
                except:
                    post_content =  None
                    # with open('data_.json' , 'a', encoding='utf-8') as f:
                        # json.dump(data_node['comet_sections']['content'], f , ensure_ascii=False , indent=4)
                    # print['story'])
            refId = data_node['post_id']
            profile_url = data_node['comet_sections']['content']['story']['wwwURL'].split('/posts/')[0]
            timestamp  = data_node['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0]['story']['creation_time']
            post_date_utc = datetime.utcfromtimestamp(timestamp).isoformat()
            stars = 5 if 'recommends' in data_node['comet_sections']['context_layout']['story']['comet_sections']['title']['story']['title']['text'] else 1
            # Replies

            feedback_data = data_node['comet_sections']['feedback']['story']['story_ufi_container']["story"]['feedback_context']['feedback_target_with_context']['comment_list_renderer']['feedback']
            comments = feedback_data['comment_rendering_instance_for_feed_location']['comments']['edges']
            total_comments = feedback_data['comment_rendering_instance']['comments']['total_count']
            review_data = {
                'refId' : str(refId),
                'stars':stars,
                'name': author_name,
                'profile': profile_url,
                'date': post_date_utc,
                'order':self.orderId,
                'content': post_content,
                'replies': []
            }

            for index , comment in enumerate(comments):
                try:
                    commenter_name  = comment['node']['user']['name']
                except Exception:
                    commenter_name  = comment['node']['author']['name']
                try:
                    comment_text = comment['node']['body_renderer']['text']
                except:
                    comment_text =  ""
                comment_timestamp  = comment['node']['created_time']
                comment_date_utc = datetime.utcfromtimestamp(comment_timestamp).isoformat()
                refId_comment = comment['node']['legacy_fbid']

                review_data['replies'].append({
                    'refId':refId_comment,
                    'name': commenter_name,
                    'date': comment_date_utc,
                    'order':index + 1,
                    'content': comment_text,
                })
            self.reviews.append(review_data)
            self.orderId += 1
    def parse_html_data(self , json_data):
        # Kiểm tra nếu "RelayPrefetchedStreamCache" tồn tại trong dữ liệu
        if any("RelayPrefetchedStreamCache" in item for item in json_data):
            # Lấy dữ liệu định dạng ban đầu từ JSON
            data_block = json_data[3][1].get('__bbox', {}).get('result', {}).get('data', {})

            # Cố gắng lấy thông tin chính (node)
            try:
                main_data = data_block['node']
            except KeyError:
                main_data = data_block['user']['ratings_list_feed_units']['reviews_feed']['edges'][0]['node']
            else:
                try:
                    main_data = data_block['user']['ratings_list_feed_units']['reviews_feed']['edges'][0]['node']
                except KeyError:
                    main_data = data_block['node']
            # with open('data_.json' , 'a', encoding='utf-8') as f:
                # json.dump(main_data, f , ensure_ascii=False , indent=4)
            
            refId = main_data['post_id']
            # Trích xuất thông tin từ dữ liệu
            stars = 5 if 'recommends' in main_data['comet_sections']['context_layout']['story']['comet_sections']['title']['story']['title']['text'] else 1
            author_name = main_data['comet_sections']['content']['story']['actors'][0]['name']
            post_content = main_data['comet_sections']['content']['story']['message']['text']
            profile_url = main_data['comet_sections']['content']['story']['wwwURL'].split('/posts/')[0]
            
            # Lấy thời gian và chuyển sang UTC
            timestamp = main_data['comet_sections']['context_layout']['story']['comet_sections']['metadata'][0]['story']['creation_time']
            post_date_utc = datetime.utcfromtimestamp(timestamp).isoformat()

            # Trích xuất nội dung bình luận
            comment_data = main_data['comet_sections']['feedback']['story']['story_ufi_container']['story']['feedback_context']['feedback_target_with_context']['comment_list_renderer']['feedback']
            
            # Tổng số bình luận
            total_comments = comment_data['comment_rendering_instance']['comments']['total_count']
            comment_edges = comment_data['comment_rendering_instance_for_feed_location']['comments']['edges']

            # Chuẩn bị cấu trúc kết quả
            post_details = {
                'refId' : refId,
                'stars':stars,
                'name': author_name,
                'profile': profile_url,
                'date': post_date_utc,
                'order':self.orderId,
                # 'total_comments': total_comments,
                'content': post_content,
                'replies': []
            }

            # Lặp qua từng bình luận và thêm vào kết quả
            for index , comment in enumerate(comment_edges):
                comment_author = comment['node']['user']['name']
                comment_text = comment['node']['body_renderer']['text']
                comment_time = comment['node']['created_time']
                comment_date_utc = datetime.utcfromtimestamp(comment_time).isoformat()
                refId_comment = comment['node']['legacy_fbid']
                post_details['replies'].append({
                    'refId':refId_comment,
                    'name': comment_author,
                    'date': comment_date_utc,
                    'order': index + 1,
                    'content': comment_text,
                })

            return post_details


def debug(self):
    ReviewScrape().run('https://www.facebook.com/chancellorsea/reviews')