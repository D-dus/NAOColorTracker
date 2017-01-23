using UnityEngine;
using System.Collections;

public class SinusMove : MonoBehaviour {

	private Vector3 mStartPosition;
	private float mTime;
	public bool isRed;
	public bool isBlue;
	public bool isYellow;
	public bool isGreen;
	public bool mIsMoving;
	void Start () 
	{
		mStartPosition = transform.position;
		mTime = 0;
	}
	
	void Update()
	{
		if (mIsMoving) {
			if (isRed)
				transform.position = mStartPosition + new Vector3 (Mathf.Sin (mTime), 0, Mathf.Cos (mTime));
			if (isBlue)
				transform.position = mStartPosition + new Vector3 (Mathf.Cos (mTime), 0, Mathf.Sin (mTime));
			if (isGreen)
				transform.position = mStartPosition + new Vector3 (Mathf.Sin (mTime * 2), 0, Mathf.Cos (mTime));
			if (isYellow)
				transform.position = mStartPosition + new Vector3 (Mathf.Sin (-mTime), 0, Mathf.Cos (mTime));
			mTime+=Time.deltaTime;
		}
	}
}
