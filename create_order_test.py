#Шапиева Екатерина, 28 когорта - дипломный проект. Инженер по тестированию плюс
import sender_stand_request as req

import data

def test_create_and_track_order():
    current_body = data.order_body.copy()

    create_response = req.post_new_body(current_body)
    assert create_response.status_code == 201

    track = create_response.json().get("track")
    assert track is not None

    get_response = req.get_order_by_track(track)
    assert get_response.status_code == 200