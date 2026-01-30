# Weekend Travel Schedule Texter

Texts your girlfriend your weekend work travel schedule every Monday morning, with a motivational quote from a famous orator.

## Setup

1. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Configure environment variables** — copy `.env.example` to `.env` and fill in:
   - Your [Twilio](https://www.twilio.com/) credentials (Account SID, Auth Token, phone number)
   - Your girlfriend's phone number

3. **Add your travel schedule** — edit `schedule_data.py` with your upcoming trips:
   ```python
   TRAVEL_SCHEDULE = [
       {
           "dates": "Feb 7-9",
           "location": "Chicago, IL",
           "purpose": "Client onsite meeting"
       },
   ]
   ```

## Usage

```bash
# Send a text right now (for testing)
python app.py

# Run as a scheduler (sends every Monday at 8 AM)
python app.py --cron
```
