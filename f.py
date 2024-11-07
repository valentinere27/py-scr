import asyncio
from pyppeteer import launch

async def take_screenshot(url):
    browser = await launch(headless=True)
    page = await browser.newPage()
    
    await page.goto(url)

    await page.waitForSelector('input[name="user"]')
    await page.type('input[name="user"]', "admin")
    await page.type('input[name="password"]', ":L;SZCP824M7__k")    

    await page.click('button[type="submit"]')
    await asyncio.sleep(2)
    
    await page.screenshot({'path': 'full_screenshot.png', 'fullPage': True})
    print("Полный скриншот сохранен как 'full_screenshot.png'")
    
    await browser.close()

url = 'http://localhost:3000/d/be38fi7fv2ebkd/new-dashboard?from=now-6h&to=now&timezone=browser'

asyncio.get_event_loop().run_until_complete(take_screenshot(url))
