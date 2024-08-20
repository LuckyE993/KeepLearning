//
// Created by luckye on 24-8-19.
//
#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/features2d/features2d.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <chrono>

using namespace std;
using namespace cv;

int main(int argc, char **argv)
{
    //读取图像
    string img1 = "../1.png";
    string img2 = "../2.png";

    Mat img_1 = imread(img1, IMREAD_COLOR);
    Mat img_2 = imread(img2, IMREAD_COLOR);
    cout <<"img_1:" <<img_1.size()<<" img_2:"<<img_2.size() << endl;
    //初始化 关键点，BRIEF描述子，检测器，描述提取，匹配器
    vector<KeyPoint> keypoints_1, keypoints_2;
    Mat descriptors_1, descriptors_2;
    Ptr<FeatureDetector> detector = ORB::create();
    Ptr<DescriptorExtractor> descriptor = ORB::create();
    Ptr<DescriptorMatcher> matcher = DescriptorMatcher::create("BruteForce-Hamming");

    // 第一步：检测 Oriented FAST角点位置
    detector->detect(img_1, keypoints_1);
    detector->detect(img_2, keypoints_2);

    // 第二步：根据角点位置计算 BRIEF描述子
    descriptor->compute(img_1, keypoints_1, descriptors_1);
    descriptor->compute(img_2, keypoints_2, descriptors_2);

    Mat output_img1;
    drawKeypoints(img_1,keypoints_1,output_img1,Scalar::all(-1),DrawMatchesFlags::DEFAULT);
    imshow("ORB",output_img1);

    // 第三步：匹配 BRIEF描述子，使用 Hamming 距离
    vector<DMatch> matches;
    matcher->match(descriptors_1, descriptors_2, matches);
    cout << "matches.size():" << matches.size() << endl;

    // 第四步：对匹配点进行筛选
    auto min_max = minmax_element(matches.begin(), matches.end(),
        [](const DMatch& m1, const DMatch& m2){return m1.distance < m2.distance;});

    double min_distance = min_max.first->distance;
    double max_distance = min_max.second->distance;

    cout<<"min_dist:"<<min_distance<<" max_dist:"<<max_distance<<endl;
    vector<DMatch> goodmatches;

    for (int i = 0; i < descriptors_1.rows; i++)
    {
        if(matches[i].distance <= max(2*min_distance,30.0))
        {
            goodmatches.push_back(matches[i]);
        }
    }

    // 第五步：绘制匹配结果
    Mat img_mat,img_good;
    drawMatches(img_1, keypoints_1, img_2, keypoints_2, goodmatches, img_good);
    imshow("good matches",img_good);
    drawMatches(img_1,keypoints_1,img_2,keypoints_2,matches,img_mat);
    imshow("normal matches",img_mat);

    waitKey(0);
    return 0;
}