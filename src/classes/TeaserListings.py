import pyshorteners
from .TeaserInstance import TeaserInstance
from ..lib.config import characterLimit

class TeaserListings:
  def __init__(self, teasers):
    self.teasers = teasers
    self.teaserInstances = []
    self.list = self.list
    self.print = self.print
    self.urlShortener = pyshorteners.Shortener()

    self.build_teaser_instances()

  def build_teaser_instances(self):
    for teaser in self.teasers:
      self.teaserInstances.append( TeaserInstance(teaser) )

  def list(self, limit = 15):
    result = ''
    total = len(self.teaserInstances)

    result += str(total) + ' OzBargain deals today: '
    result += '\n'
    result += '\n'

    for teaser in self.teaserInstances:
      if teaser.title and teaser.link:
        result += " ".join(teaser.title.split()[:limit])
        result += '\n'
        result += self.urlShortener.tinyurl.short(teaser.link)
        result += '\n'
        result += '\n'

    if (self.character_limit_exceeded(result)):
      return self.list(limit - 1)
    else:
      return result

  def character_limit_exceeded(self, payload):
    return len(payload) > characterLimit

  def print(self):
    print(self.list())