using UnityEngine;
using System.Collections;

public class ColorTrackerMovement : MonoBehaviour {


	[SerializeField]
	private Transform mMotorX;
	
	[SerializeField]
	private Transform mMotorY;

	public void ChangeRotation(float iCommand)
	{
		mMotorY.Rotate (0, iCommand, 0);
	}
	public void ChangeRotationX(float iCommand)
	{
		mMotorX.Rotate (iCommand, 0, 0);
	}
}
