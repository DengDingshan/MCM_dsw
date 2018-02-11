class SelfAffineParameters:
    def __init__(self):
        self.hrms = 1
        self.dimensions = (1, 1)
        self.hurst = [0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]
        self.lambda_L_over_lambda_0 = None
        self.lambda_L_over_lambda_1 = None