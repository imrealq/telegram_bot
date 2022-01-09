import logging
import requests
import datetime

from database import (
    session, HackerNewsDateTime, HackerNewsTopStories)

from generic import (
    AMOUNT, HACKER_NEW_FIREBASE, HACKER_NEW_ITEM_URL)


logging.basicConfig(level=logging.DEBUG, filename='apps.log', filemode='w')
logger = logging.getLogger()

def get_stories(as_of, type='beststories'):
    url = HACKER_NEW_FIREBASE + f"{type}.json"
    resp = requests.get(url)
    if resp.ok:
        list_stories_item = resp.json()[: AMOUNT]
        for item in list_stories_item:
            story_endpoint = HACKER_NEW_FIREBASE + f'item/{item}.json'
            story_resp = requests.get(story_endpoint)
            if story_resp.ok:
                story_info = story_resp.json()
                data = {
                    f'story_{key}': story_info.get(key) 
                    for key in ('id', 'title', 'url', 'score')}
                data.update({'as_of_id': as_of.id, 'story_type': type})
                if not story_info.get('url'):
                    data['story_url'] = (
                        HACKER_NEW_ITEM_URL + f"{story_info['id']}")
                session.add(HackerNewsTopStories(**data))
    else:
        logging.info('Could not get from HN')


def get_stories_message():
    as_of = session.query(
        HackerNewsDateTime).order_by(HackerNewsDateTime.as_of.desc()).first()
    stories = session.query(HackerNewsTopStories)\
        .filter_by(as_of_id=as_of.id)\
        .order_by(
            HackerNewsTopStories.story_type,
            HackerNewsTopStories.story_score.desc())
    resp = f"""**Updated at: {as_of.as_of.strftime("%m/%d/%Y, %H:%M:%S")}**\n\n"""
    count = 0
    for s in stories:
        if count == 0:
            resp += '---HOTTEST---\n'
        elif count == 5:
            resp += '---NEWEST---\n'
        resp += f"[{s.story_title}] - point: {s.story_score}\n{s.story_url}\n\n"
        count += 1
    return resp

def main():
    as_of = HackerNewsDateTime(as_of=datetime.datetime.now())
    session.add(as_of)
    session.flush()
    get_stories(as_of, 'beststories')
    get_stories(as_of, 'newstories')
    session.commit()


if __name__ == '__main__':
    main()

