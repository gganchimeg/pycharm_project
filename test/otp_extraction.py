from datetime import datetime, timedelta
import re
import subprocess


def otp_extraction():
    epoch_time_5_minutes_before = (int((datetime.now() - timedelta(seconds=20)).timestamp()) * 1000)
    print("epoch time: ",epoch_time_5_minutes_before)
    adb_query = f"content query --uri content://sms/inbox --projection body --where 'date>{epoch_time_5_minutes_before} AND address=\"1474\"' --sort \"date\""

    try:
        result = subprocess.run(["adb","shell", adb_query],
                                capture_output=True,
                                encoding="UTF-8",
                                check=True)

        result = result.stdout.strip().split('\n')[-1]
        print("result: ", result)
        # code extract
        pattern = r".*: .*: (.*)"
        match = re.search(pattern, result)
        if match:
            extracted_value = match.group(1)
            print(extracted_value)
            return int(extracted_value)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Error output: {e.stderr}")
        return e.stderr




