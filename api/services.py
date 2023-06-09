from django.http import JsonResponse
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def scrape_url(session, url):
    async with session.get(url) as response:
        

def scrape(request):
    return JsonResponse({'message': 'success'})