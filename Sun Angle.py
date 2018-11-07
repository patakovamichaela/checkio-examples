"""this is my solution of Chekio mission Sun Angle (https://py.checkio.org/en/mission/sun-angle/)

Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun rises
in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith, which
means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees. If the input
will be the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!"."""

from datetime import datetime
srise  = datetime.strptime("06:00",'%H:%M')
sset = datetime.strptime("18:00",'%H:%M')
def sun_angle(time):
    time_stamp = datetime.strptime(time,'%H:%M')
    if time_stamp < srise or time_stamp >sset:
        return "I don't see the sun!"
    else:
        angle = ((time_stamp - srise).total_seconds()/60)/4
        return angle

# These tests was created by Chekio.

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
