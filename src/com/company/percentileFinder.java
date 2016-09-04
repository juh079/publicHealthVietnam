package com.company;

/**
 * Created by JHuynh on 9/1/16.
 */
public class percentileFinder {
    private int findAge( double age ){
        //use age to find appropriate subarray
        int ageIndex = -1;
        double[] ages = { 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144 };
        double ageInMonths = age * 12;
        for (int i = 0; i < 12; i++) {
            double ageDifference = ageInMonths - ages[i];
            if( ageDifference <= 0 && i > 0){
                if(ageDifference < -6 ){
                    ageIndex = i-1;
                }
                else {
                    ageIndex = i; //assign to appropriate weight/height array
                }
                break; //end loop
            }
        }
        return ageIndex;
    }

    public int getAge(double age){
        return findAge(age);
    }

    private double findPercentile( double[][] metrics, double heightOrWeight, int ageIndex ){
        double percentile = 99;
        int[] percentiles = { 3, 5, 10, 25, 50, 75, 90, 95, 97 };
        for (int i = 0; i < 9; i++) {
            double metricsDifference = heightOrWeight - metrics[ageIndex][i];
            if( metricsDifference == 0 ){
                return percentiles[i];
            }
            else if( metricsDifference < 0 ){
                if( i == 0 ) //if our measurement is less than the first value(3%) we assume 1%
                    return 1;
                double variationFromStandardPercentiles =
                        (heightOrWeight - metrics[ageIndex][i-1])/
                                (metrics[ageIndex][i] - metrics[ageIndex][i-1]);
                percentile = ((percentiles[i] - percentiles[i-1]) * variationFromStandardPercentiles)
                        + percentiles[i-1];
                //System.out.println(variationFromStandardPercentiles + " " + percentile + " " + percentiles[i-1] + " " + ageIndex);
                return percentile;
            }
        }
        return percentile;
    }

    public double getPercentile(double[][] metrics, double heightOrWeight, int ageIndex){
        return findPercentile(metrics, heightOrWeight, ageIndex);
    }
}
