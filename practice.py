def increment(self, seconds):
    seconds += self.time_to_int()
    return int_to_time(seconds)
  
 def is_after(self, other):
     return self.time_to_int() > other.time_to_int()
  
  end.is_after(start)
