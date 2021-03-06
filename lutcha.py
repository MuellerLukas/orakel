# -*- coding: utf-8 -*-
# vim:set ts=8 sts=8 sw=8 tw=80 noet:

from module import Module, MUC
from urllib.parse import quote as urlencode

class Lutcha(Module):
	def __init__(self, **keywords):
		super(Lutcha, self).__init__([MUC], name=__name__, **keywords)

	def muc_msg(self, msg, **keywords):
		parts = msg.strip().split(' ', 1)
		if len(parts) == 2 and parts[0][0] == "!" and \
				parts[0][1:].lower() in ["bash", "doc", "lutcha"]:
			result = self.handle(parts[0][1:].lower(), parts[1])
			if result:
				self.send_muc(result)

	def handle(self, cmd, msg):
		parts = msg.strip().split(' ', 1)
		url = "https://lutcha.de"
		prefix = "bash " if cmd == "bash" else ""
		if len(parts) == 2 and parts[0][0] == "-":
			if parts[0] == "--":
				return "%s/%s" % (url,
						urlencode(parts[1].strip()))
			return "%s/%s/%s" % (url,
					urlencode(parts[0].lstrip("-")),
					urlencode(prefix + parts[1].strip()))
		elif len(parts) == 1:
			return "%s/%s" % (url, urlencode(prefix + msg.strip()))
		else:
			return "%s/%s" % (url, urlencode(prefix +
					" ".join(parts)))
