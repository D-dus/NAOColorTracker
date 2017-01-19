using UnityEngine;
using System.Collections;

public class SphereControl : MonoBehaviour {


	private float mXInput;
	private float mYInput;
	public float speed;
	private Rigidbody mRigidbody;
	public bool mIsXY;
	// Use this for initialization
	void Start()
	{
		mRigidbody = GetComponent<Rigidbody> ();
	}
	// Update is called once per frame
	void Update () 
	{
		ApplyMovement (mXInput, mYInput,mRigidbody	);
	}

	void FixedUpdate()
	{

		
	}
	public void ApplyMovement(float iXPosition, float iYPosition,Rigidbody iRb)
	{
		Vector3 lMovement;
		if(mIsXY)
			lMovement=new Vector3(Input.GetAxis("Horizontal")*Time.deltaTime,Input.GetAxis("Vertical")*Time.deltaTime,0);
		else
			lMovement = new Vector3 (Input.GetAxis ("Horizontal")*Time.deltaTime, 0, Input.GetAxis ("Vertical")*Time.deltaTime);
		transform.Translate (lMovement*speed);
	}
}
