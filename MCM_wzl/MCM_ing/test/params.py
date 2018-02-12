class SelfAffineParameters:
    def __init__(self, hrms, hurst):
        self.hrms = hrms
        self.dimensions = (1, 1)
        self.hurst = hurst
        self.lambda_L_over_lambda_0 = None
        self.lambda_L_over_lambda_1 = None