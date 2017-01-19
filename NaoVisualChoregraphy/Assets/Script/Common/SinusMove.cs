using UnityEngine;
using System.Collections;

public class SinusMove : MonoBehaviour {

	private Vector3 mStartPosition;
	public bool isRed;
	public bool isBlue;
	public bool isYellow;
	public bool isGreen;
	void Start () 
	{
		mStartPosition = transform.position;
	}
	
	void Update()
	{
		if(isRed)
			transform.position = mStartPosition + new Vector3(Mathf.Sin(Time.time), 0,Mathf.Cos(Time.time));
		if(isBlue)
			transform.position = mStartPosition + new Vector3(Mathf.Cos(Time.time), 0,Mathf.Sin(Time.time));
		if(isGreen)
			transform.position = mStartPosition + new Vector3(Mathf.Sin(Time.time*2), 0,Mathf.Cos(Time.time));
		if(isYellow)
			transform.position = mStartPosition + new Vector3(Mathf.Sin(-Time.time), 0,Mathf.Cos(Time.time));
	}
}
