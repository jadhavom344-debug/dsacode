class CallCenterQueue:
    def _init_(self):
        self.queue = []

    def addCall(self, customerID, callTime):
        call = {
            "customerID": customerID,
            "callTime": callTime
        }
        self.queue.append(call)
        print(f"Call added: {call}")

    def answerCall(self):
        if self.isQueueEmpty():
            print("No calls to answer. Queue is empty!")
            return None
        answered_call = self.queue.pop(0)
        print(f"Answered call: {answered_call}")
        return answered_call

    def viewQueue(self):
        if self.isQueueEmpty():
            print("Queue is empty.")
        else:
            print("Current Call Queue:")
            for call in self.queue:
                print(call)

    def isQueueEmpty(self):
        return len(self.queue) == 0


# ------------------------------------
# Program Execution (Sample Output)
# ------------------------------------

cc = CallCenterQueue()

cc.addCall(101, 5)
cc.addCall(102, 3)
cc.addCall(103, 4)

cc.viewQueue()

cc.answerCall()
cc.answerCall()

cc.viewQueue()

print("Is queue empty?", cc.isQueueEmpty())

cc.answerCall()
print("Is queue empty now?", cc.isQueueEmpty())
