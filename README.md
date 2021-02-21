## Inspiration
We all know where the Electoral College has preference (Wyoming Nebraska etc.), but we also know WHO the electoral college prefers
## What it does
Based purely off someones image, we can predict their race, age, and gender and correspondingly provide average disenfranchisement for that demographics from the past 10 years

## How we built it
We built this with a Flask application in tandem with the ClarafAI API. We connected that with a Pandas API call to our database of disenfranchisements to pull the average disenfranchisement over the past 10 years

## Challenges we ran into
It was our first time working with Flask, so we had a ton of compatibility issues

## Accomplishments that we're proud of
It's pretty amazing that based purely off an image, a computer can predict someone's race, age, and gender just like that. I also think it's kind of fascinating how we can connect that with publically available info (like census data), to show how it affects somebody.

## What we learned
How to use Flask, ClarafAI, in connection with Pandas.

## What's next for How the US Sees us
We want to make it prettier (pretty obvious we aren't web development guys), as well as start to develop our OWN CNN's to predict this stuff, rather than use an API
