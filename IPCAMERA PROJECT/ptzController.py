from onvif import ONVIFCamera

class PTZController:
    def __init__(self, ip, port, user, passwd):
        self.mycam = ONVIFCamera(ip, port, user, passwd)
        self.media = self.mycam.create_media_service()
        self.ptz = self.mycam.create_ptz_service()
        self.media_profile = self.media.GetProfiles()[0]
        self.token = self.media_profile.token
        self.settedX=0.0
        self.settedY=0.0
        self.settedZoom=0.0
        self.xnow=0.0
        self.ynow=0.0
        self.zoomx=0.0
        self.status=False
    def checker(self):
        if not self.status:
            self.status = True
            self.myAbsoluteMove(0, 0)
            self.printStatus()
        else:
            self.printStatus()

    def myContinuousMove(self, pan, tilt, zoom):
        request = self.ptz.create_type('ContinuousMove')
        request.ProfileToken = self.token

        if request.Velocity is None:
            request.Velocity = self.ptz.GetStatus({'ProfileToken': self.token}).Position
            
        request.Velocity.PanTilt.x = pan
        request.Velocity.PanTilt.y = tilt
        request.Velocity.Zoom.x = zoom
        self.xnow=pan
        self.ynow=tilt
        self.ptz.ContinuousMove(request)
    
    def getX(self):
        return self.xnow
    def getY(self):
        return self.ynow
    
    def myAbsoluteMove(self,pan,tilt,zoom=0.0):
        request=self.ptz.create_type('AbsoluteMove')
        request.ProfileToken=self.token
        request.Position = self.ptz.GetStatus({'ProfileToken': self.token}).Position
        request.Position.PanTilt.x=pan
        request.Position.PanTilt.y=tilt
        request.Position.Zoom.x = zoom
        self.ptz.AbsoluteMove(request)
        self.xnow=pan
        self.ynow=tilt
    
    def myRelativeMove(self, pan, tilt):
        request= self.ptz.create_type('RelativeMove')
        request.ProfileToken = self.token
        request.Translation = self.ptz.GetStatus({'ProfileToken': self.token}).Position
        request.Translation.PanTilt.x = pan
        request.Translation.PanTilt.y = tilt
        self.ptz.RelativeMove(request)
        