from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict , Annotated,Optional,Literal
import os
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

model= ChatGroq(model='qwen/qwen3.8-27b', api_key=api_key)

class Review(TypedDict):
    key_theme:Annotated[list[str],"write down all the key theme discussed in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["positive", "negative"], "The sentiment of the review, either 'positive' or 'negative'"]
    pros:Annotated[Optional[list[str]], "List down all the pros mentioned in the review"]
    cons:Annotated[Optional[list[str]], "List down all the cons mentioned in the review"]

structured_model=model.with_structured_output(Review)    #structure se ek prompt generate hota h jisse model ko input diya jata h aur model ka output structured format me aata h

result=structured_model.invoke("""**The Apple iPhone Duo: A Three-Lakh Rupee Identity Crisis**

Apple's "Surprise and Shine" event in September 2026 finally delivered the company's long-rumored foldable. Powered by the 2nm A20 Pro chip and featuring a 5.4-inch outer display that unfolds into a 7.6-inch inner canvas, the iPhone Duo is engineered to turn heads. But after living with the device, a harsh reality sets in: this is an exhaustingly compromised first-generation experiment masquerading as an ultra-premium flagship.

Let’s start with the physical toll. Despite utilizing a premium titanium frame, the Duo is undeniably heavy, feeling like an absolute anchor in your pocket during daily carry. The ergonomics are fundamentally flawed for everyday tasks. Whenever you need to type on the unfolded screen, the device instantly feels cumbersome and practically demands two-handed use in any orientation. You are constantly wrestling with its bulky form factor rather than enjoying it. Even the biometric security feels like a regression—Apple opted for a side-button Touch ID that introduces so much friction that bypassing it entirely via "Unlock with Apple Watch" is noticeably faster.

The software ecosystem feels equally half-baked. Shipped with iOS 27.1, the Duo attempts to bring iPad-inspired UI elements to a foldable, but it trips over a severe lack of third-party app optimization. If an app hasn't been updated to the latest SDK, you are forced to stare at pillarboxed black bars or glaring blank spaces on the right side of the screen. Booting up staple communication apps like Telegram on the massive inner display leaves you with a portrait-oriented window swimming in awkward dead space. Furthermore, despite the sprawling screen real estate, Apple limits multitasking to just two side-by-side apps. It ultimately delivers 60% of an iPhone and 60% of an iPad, failing to master the utility of either.

Perhaps the most egregious compromise is the camera system. You are paying for Apple's most expensive iPhone ever, yet you are only given a dual rear camera setup that produces strictly "fine," middling quality. The lenses simply will not blow you away in low-light situations, falling woefully short of the photographic prowess found in the standard iPhone 18 Pro line. Taking photos with the unfolded device also feels ergonomically terrible.

This brings us to the ultimate dealbreaker: the cost. In India, the base 256GB model demands an astronomical Rs. 2,99,900, scaling up to a farcical Rs. 4,49,900 for the 2TB variant. For that exorbitant price, you are not buying the polished future of smartphones. You are personally funding Apple's beta test, sacrificing elite camera optics, ergonomic comfort, and software coherence for a folding screen.""")

print(result)