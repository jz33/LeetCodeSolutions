def numUniqueEmails(emails: List[str]) -> int:       
      addressBook = set()
      for email in emails:
          local, domain = email.split('@')
          plusIndex = local.find('+')
          if plusIndex != -1:
              local = local[:plusIndex]
          addressBook.add(local.replace('.', '') + '@' + domain)      
      return len(addressBook)
